from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
RUNNER = REPO_ROOT / "tools" / "run_tests.py"


class ProblemRunnerTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.repo = Path(self.temp_dir.name)

    def tearDown(self):
        self.temp_dir.cleanup()

    def run_runner(self):
        return subprocess.run(
            [sys.executable, str(RUNNER), "--root", str(self.repo)],
            text=True,
            capture_output=True,
            check=False,
        )

    def test_runs_python_tests_by_importing_solution_path_and_lists_untested(self):
        python_problem = self.repo / "0001-path-import"
        python_problem.mkdir()
        (python_problem / "solution-with-hyphen.py").write_text(
            "class Solution:\n"
            "    def add(self, left, right):\n"
            "        return left + right\n",
            encoding="utf-8",
        )
        (python_problem / "tests.py").write_text(
            "def run(solution):\n"
            "    solver = solution.Solution()\n"
            "    assert solver.add(2, 3) == 5\n"
            "    assert solver.add(-1, 1) == 0\n",
            encoding="utf-8",
        )
        untested = self.repo / "plain-untested"
        untested.mkdir()
        (untested / "answer.js").write_text("const answer = 42;\n", encoding="utf-8")

        result = self.run_runner()

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("PASS 0001-path-import [Python]", result.stdout)
        self.assertIn("UNTESTED plain-untested", result.stdout)
        self.assertIn("Summary: 1 passed, 0 failed, 1 untested", result.stdout)
        self.assertFalse((python_problem / "__pycache__").exists())

    def test_python_assertion_failure_exits_nonzero(self):
        problem = self.repo / "0002-failing-case"
        problem.mkdir()
        (problem / "solution.py").write_text(
            "class Solution:\n    def value(self):\n        return 1\n", encoding="utf-8"
        )
        (problem / "tests.py").write_text(
            "def run(solution):\n"
            "    assert solution.Solution().value() == 2, 'example mismatch'\n",
            encoding="utf-8",
        )

        result = self.run_runner()

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("FAIL 0002-failing-case [Python]", result.stdout)
        self.assertIn("AssertionError: example mismatch", result.stderr)
        self.assertIn("Summary: 0 passed, 1 failed, 0 untested", result.stdout)

    @unittest.skipUnless(shutil.which("g++"), "g++ is required for the C++ runner test")
    def test_compiles_solution_and_paired_cpp_tests_as_cpp20(self):
        problem = self.repo / "0003-cpp20"
        problem.mkdir()
        (problem / "0003-cpp20.cpp").write_text(
            "#include <span>\n"
            "class Solution {\n"
            "public:\n"
            "    int sum(std::span<const int> values) {\n"
            "        int total = 0;\n"
            "        for (int value : values) total += value;\n"
            "        return total;\n"
            "    }\n"
            "};\n",
            encoding="utf-8",
        )
        (problem / "tests_cpp.cpp").write_text(
            "#include <array>\n"
            "#include <cassert>\n"
            "int main() {\n"
            "    std::array<int, 3> values{1, 2, 3};\n"
            "    assert(Solution().sum(values) == 6);\n"
            "}\n",
            encoding="utf-8",
        )

        result = self.run_runner()

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("PASS 0003-cpp20 [C++]", result.stdout)
        self.assertIn("Summary: 1 passed, 0 failed, 0 untested", result.stdout)

    def test_test_file_without_matching_solution_is_a_failure(self):
        problem = self.repo / "0004-mismatched-test"
        problem.mkdir()
        (problem / "solution.py").write_text("class Solution:\n    pass\n", encoding="utf-8")
        (problem / "tests_cpp.cpp").write_text("int main() {}\n", encoding="utf-8")

        result = self.run_runner()

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("FAIL 0004-mismatched-test [C++]", result.stdout)
        self.assertIn("tests_cpp.cpp found without a C++ solution", result.stderr)


if __name__ == "__main__":
    unittest.main()
