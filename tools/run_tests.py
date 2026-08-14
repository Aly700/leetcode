#!/usr/bin/env python3
"""Discover and run per-problem Python and C++ example tests."""

from __future__ import annotations

import argparse
from contextlib import contextmanager
from dataclasses import dataclass
import importlib.util
import os
from pathlib import Path
import shutil
import typing
import subprocess
import sys
import tempfile
import traceback
from types import ModuleType

from generate_index import IGNORED_DIRECTORIES, solution_files


CPP_SUFFIXES = {".cc", ".cpp", ".cxx"}


@dataclass(frozen=True)
class SuiteResult:
    problem: str
    language: str
    passed: bool
    details: str = ""


@contextmanager
def working_directory(path: Path):
    previous = Path.cwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(previous)


@contextmanager
def suppress_bytecode():
    previous = sys.dont_write_bytecode
    sys.dont_write_bytecode = True
    try:
        yield
    finally:
        sys.dont_write_bytecode = previous


def load_module(path: Path, name: str) -> ModuleType:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"cannot create an import spec for {path}")
    module = importlib.util.module_from_spec(spec)
    # LeetCode solution files use typing names without importing them.
    for typing_name in ("List", "Dict", "Optional", "Tuple", "Set", "Deque"):
        setattr(module, typing_name, getattr(typing, typing_name))
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def python_suite(problem: Path, ordinal: int) -> SuiteResult:
    python_solutions = [path for path in solution_files(problem) if path.suffix.lower() == ".py"]
    if not python_solutions:
        return SuiteResult(
            problem.name,
            "Python",
            False,
            "tests.py found without a Python solution",
        )

    solution_name = f"leetcode_solution_{ordinal}"
    tests_name = f"leetcode_tests_{ordinal}"
    try:
        with suppress_bytecode(), working_directory(problem):
            solution = load_module(python_solutions[0], solution_name)
            tests = load_module(problem / "tests.py", tests_name)
            run = getattr(tests, "run", None)
            if not callable(run):
                raise TypeError("tests.py must define callable run(solution)")
            run(solution)
    except BaseException:
        return SuiteResult(problem.name, "Python", False, traceback.format_exc().rstrip())
    finally:
        sys.modules.pop(solution_name, None)
        sys.modules.pop(tests_name, None)
    return SuiteResult(problem.name, "Python", True)


def include_path(path: Path) -> str:
    return path.resolve().as_posix().replace("\\", "\\\\").replace('"', '\\"')


def cpp_suite(problem: Path, timeout: float) -> SuiteResult:
    cpp_solutions = [
        path for path in solution_files(problem) if path.suffix.lower() in CPP_SUFFIXES
    ]
    if not cpp_solutions:
        return SuiteResult(
            problem.name,
            "C++",
            False,
            "tests_cpp.cpp found without a C++ solution",
        )

    compiler = shutil.which("g++")
    if compiler is None:
        return SuiteResult(problem.name, "C++", False, "g++ was not found on PATH")

    try:
        with tempfile.TemporaryDirectory(prefix="leetcode-cpp-") as temp_name:
            temp_dir = Path(temp_name)
            wrapper = temp_dir / "suite.cpp"
            binary = temp_dir / "suite"
            wrapper.write_text(
                f'#include "{include_path(cpp_solutions[0])}"\n'
                f'#include "{include_path(problem / "tests_cpp.cpp")}"\n',
                encoding="utf-8",
            )
            compiled = subprocess.run(
                [compiler, "-std=c++20", str(wrapper), "-o", str(binary)],
                cwd=problem,
                text=True,
                capture_output=True,
                timeout=timeout,
                check=False,
            )
            if compiled.returncode != 0:
                details = compiled.stderr.strip() or compiled.stdout.strip()
                return SuiteResult(
                    problem.name,
                    "C++",
                    False,
                    "C++ compilation failed" + (f":\n{details}" if details else ""),
                )
            executed = subprocess.run(
                [str(binary)],
                cwd=problem,
                text=True,
                capture_output=True,
                timeout=timeout,
                check=False,
            )
            if executed.returncode != 0:
                details = executed.stderr.strip() or executed.stdout.strip()
                return SuiteResult(
                    problem.name,
                    "C++",
                    False,
                    f"C++ tests exited with status {executed.returncode}"
                    + (f":\n{details}" if details else ""),
                )
    except subprocess.TimeoutExpired:
        return SuiteResult(problem.name, "C++", False, f"C++ suite timed out after {timeout:g}s")
    except OSError:
        return SuiteResult(problem.name, "C++", False, traceback.format_exc().rstrip())
    return SuiteResult(problem.name, "C++", True)


def problem_directories(root: Path) -> list[Path]:
    return [
        directory
        for directory in sorted(root.iterdir(), key=lambda path: path.name.casefold())
        if directory.is_dir()
        and not directory.name.startswith(".")
        and directory.name not in IGNORED_DIRECTORIES
        and solution_files(directory)
    ]


def run_all(root: Path, timeout: float) -> int:
    results: list[SuiteResult] = []
    untested = 0
    python_ordinal = 0

    for problem in problem_directories(root):
        has_python_tests = (problem / "tests.py").is_file()
        has_cpp_tests = (problem / "tests_cpp.cpp").is_file()
        if not has_python_tests and not has_cpp_tests:
            print(f"UNTESTED {problem.name}")
            untested += 1
            continue
        if has_python_tests:
            python_ordinal += 1
            results.append(python_suite(problem, python_ordinal))
        if has_cpp_tests:
            results.append(cpp_suite(problem, timeout))

    for result in results:
        status = "PASS" if result.passed else "FAIL"
        print(f"{status} {result.problem} [{result.language}]")
        if result.details:
            print(f"{result.problem} [{result.language}]:\n{result.details}", file=sys.stderr)

    passed = sum(result.passed for result in results)
    failed = len(results) - passed
    print(f"Summary: {passed} passed, {failed} failed, {untested} untested")
    return 1 if failed else 0


def parse_args(arguments: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--timeout",
        type=float,
        default=10.0,
        help="seconds allowed for C++ compilation and execution (default: 10)",
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help=argparse.SUPPRESS,
    )
    args = parser.parse_args(arguments)
    if args.timeout <= 0:
        parser.error("--timeout must be positive")
    return args


def main(arguments: list[str] | None = None) -> int:
    args = parse_args(arguments)
    try:
        return run_all(args.root.resolve(), args.timeout)
    except OSError as error:
        print(f"error: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
