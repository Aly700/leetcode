#!/usr/bin/env python3
"""Generate the repository problem manifest and README index."""

from __future__ import annotations

import argparse
import ast
from dataclasses import dataclass
from datetime import datetime, timezone
import html
import json
import os
from pathlib import Path
import re
import sys
from urllib.parse import quote


INDEX_BEGIN = "<!-- INDEX:BEGIN -->"
INDEX_END = "<!-- INDEX:END -->"

LANGUAGE_BY_SUFFIX = {
    ".c": "C",
    ".cc": "C++",
    ".cpp": "C++",
    ".cxx": "C++",
    ".cs": "C#",
    ".dart": "Dart",
    ".ex": "Elixir",
    ".exs": "Elixir",
    ".go": "Go",
    ".java": "Java",
    ".js": "JavaScript",
    ".jsx": "JavaScript",
    ".kt": "Kotlin",
    ".kts": "Kotlin",
    ".php": "PHP",
    ".py": "Python",
    ".rb": "Ruby",
    ".rs": "Rust",
    ".scala": "Scala",
    ".sh": "Bash",
    ".sql": "SQL",
    ".swift": "Swift",
    ".ts": "TypeScript",
    ".tsx": "TypeScript",
}

NON_SOLUTION_NAMES = {"tests.py", "tests_cpp.cpp"}
IGNORED_DIRECTORIES = {"build", "dist", "docs", "node_modules", "tests", "tools"}
DIFFICULTIES = {"easy": "Easy", "medium": "Medium", "hard": "Hard"}
NUMBERED_DIRECTORY = re.compile(r"^(?P<id>\d+)-(?P<slug>.+)$")
PROBLEM_URL = re.compile(
    r"https?://(?:www\.)?leetcode\.com/problems/(?P<slug>[a-z0-9-]+)",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class Problem:
    id: int | None
    slug: str
    title: str
    difficulty: str
    topics: tuple[str, ...]
    languages: tuple[str, ...]
    path: str
    url: str
    solution_path: str
    tested: bool

    def as_json(self) -> dict[str, object]:
        return {
            "id": self.id,
            "slug": self.slug,
            "title": self.title,
            "difficulty": self.difficulty,
            "topics": list(self.topics),
            "languages": list(self.languages),
            "path": self.path,
            "url": self.url,
        }


def strip_tags(value: str) -> str:
    value = re.sub(r"<[^>]+>", "", value)
    return html.unescape(value).strip()


def split_numbered_title(value: str) -> tuple[int | None, str]:
    cleaned = strip_tags(value).lstrip("# ").strip()
    match = re.match(r"^(\d+)\.\s*(.+)$", cleaned)
    if match:
        return int(match.group(1)), match.group(2).strip()
    return None, cleaned


def unique(values: list[str]) -> list[str]:
    result: list[str] = []
    seen: set[str] = set()
    for value in values:
        cleaned = html.unescape(value).strip().strip("`*_# ")
        key = cleaned.casefold()
        if cleaned and key not in seen:
            result.append(cleaned)
            seen.add(key)
    return result


def parse_inline_list(value: str) -> list[str]:
    inner = value[1:-1].strip()
    if not inner:
        return []
    return [str(parse_yaml_scalar(item.strip())) for item in inner.split(",")]


def parse_yaml_scalar(value: str) -> object:
    value = value.strip()
    if value.startswith("[") and value.endswith("]"):
        return parse_inline_list(value)
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        try:
            return ast.literal_eval(value)
        except (SyntaxError, ValueError) as error:
            raise ValueError(f"invalid quoted value: {value}") from error
    if re.fullmatch(r"\d+", value):
        return int(value)
    if value.lower() in {"null", "none", "~"}:
        return None
    return value


def parse_meta_yaml(path: Path) -> dict[str, object]:
    """Parse the small top-level YAML subset used by per-problem metadata."""
    if not path.exists():
        return {}

    result: dict[str, object] = {}
    active_list: str | None = None
    for line_number, raw_line in enumerate(
        path.read_text(encoding="utf-8").splitlines(), start=1
    ):
        stripped = raw_line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if stripped.startswith("- "):
            if active_list is None:
                raise ValueError(f"{path}:{line_number}: list item has no key")
            list_value = result[active_list]
            if not isinstance(list_value, list):
                raise ValueError(f"{path}:{line_number}: invalid list")
            list_value.append(str(parse_yaml_scalar(stripped[2:].strip())))
            continue
        if raw_line[:1].isspace():
            raise ValueError(f"{path}:{line_number}: unsupported nested mapping")
        if ":" not in stripped:
            raise ValueError(f"{path}:{line_number}: expected 'key: value'")
        key, raw_value = stripped.split(":", 1)
        key = key.strip()
        raw_value = raw_value.strip()
        if not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_-]*", key):
            raise ValueError(f"{path}:{line_number}: invalid key {key!r}")
        if not raw_value:
            result[key] = []
            active_list = key
        else:
            result[key] = parse_yaml_scalar(raw_value)
            active_list = None
    return result


def parse_readme(text: str) -> dict[str, object]:
    metadata: dict[str, object] = {}
    url_match = PROBLEM_URL.search(text)
    if url_match:
        metadata["slug"] = url_match.group("slug").lower()

    html_link = re.search(
        r"<a\b[^>]*href=[\"'][^\"']*leetcode\.com/problems/[a-z0-9-]+/?[^\"']*[\"'][^>]*>"
        r"(?P<title>.*?)</a>",
        text,
        re.IGNORECASE | re.DOTALL,
    )
    markdown_link = re.search(
        r"\[(?P<title>[^\]]+)\]\(\s*https?://(?:www\.)?leetcode\.com/problems/"
        r"[a-z0-9-]+/?[^)]*\)",
        text,
        re.IGNORECASE,
    )
    title_match = html_link or markdown_link
    if title_match:
        problem_id, title = split_numbered_title(title_match.group("title"))
        if problem_id is not None:
            metadata["id"] = problem_id
        if title:
            metadata["title"] = title

    difficulty_match = re.search(
        r"<h3\b[^>]*>\s*(Easy|Medium|Hard)\s*</h3>", text, re.IGNORECASE
    )
    if not difficulty_match:
        difficulty_match = re.search(
            r"(?im)^\s*(?:[-*]\s*)?(?:\*\*)?Difficulty(?:\*\*)?\s*:\s*"
            r"(Easy|Medium|Hard)\b",
            text,
        )
    if difficulty_match:
        metadata["difficulty"] = DIFFICULTIES[difficulty_match.group(1).lower()]

    topics: list[str] = []
    topics_marker = re.search(
        r"<!---?\s*LeetCode Topics Start\s*-->(.*?)"
        r"<!---?\s*LeetCode Topics End\s*-->",
        text,
        re.IGNORECASE | re.DOTALL,
    )
    if topics_marker:
        topics.extend(
            re.findall(r"(?m)^\s*#{2,6}\s+(.+?)\s*$", topics_marker.group(1))
        )

    for match in re.finditer(
        r"<a\b[^>]*href=[\"'][^\"']*/(?:tag|topic)/[a-z0-9-]+/?[^\"']*[\"'][^>]*>"
        r"(?P<topic>.*?)</a>",
        text,
        re.IGNORECASE | re.DOTALL,
    ):
        topics.append(strip_tags(match.group("topic")))

    topics_line = re.search(
        r"(?im)^\s*(?:[-*]\s*)?(?:\*\*)?Topics(?:\*\*)?\s*:\s*(.+)$", text
    )
    if topics_line:
        topics.extend(re.split(r"\s*[,|]\s*", topics_line.group(1)))

    if not topics:
        topics_section = re.search(
            r"(?ims)^\s*#{1,6}\s+(?:LeetCode\s+)?Topics\s*$\n"
            r"(?P<body>.*?)(?=^\s*#{1,6}\s+|\Z)",
            text,
        )
        if topics_section:
            topics.extend(
                re.findall(r"(?m)^\s*(?:[-*]\s+|#{2,6}\s+)(.+?)\s*$", topics_section.group("body"))
            )

    topics = unique([strip_tags(topic) for topic in topics])
    if topics:
        metadata["topics"] = topics
    return metadata


def solution_files(directory: Path) -> list[Path]:
    files = [
        path
        for path in directory.iterdir()
        if path.is_file()
        and path.name not in NON_SOLUTION_NAMES
        and path.suffix.lower() in LANGUAGE_BY_SUFFIX
    ]

    def rank(path: Path) -> tuple[int, str]:
        if path.stem == directory.name:
            return (0, path.name.casefold())
        if path.stem.casefold() in {"solution", "answer"}:
            return (1, path.name.casefold())
        return (2, path.name.casefold())

    return sorted(files, key=rank)


def normalize_difficulty(value: object) -> str:
    if value is None or value == "":
        return "Unknown"
    normalized = DIFFICULTIES.get(str(value).strip().lower())
    if normalized is None:
        raise ValueError(f"invalid difficulty {value!r}; expected Easy, Medium, or Hard")
    return normalized


def topics_from(value: object) -> tuple[str, ...]:
    if value is None:
        return ()
    if isinstance(value, str):
        values = re.split(r"\s*[,|]\s*", value)
    elif isinstance(value, list):
        values = [str(item) for item in value]
    else:
        raise ValueError("topics must be a string or list")
    return tuple(unique(values))


def problem_from_directory(directory: Path) -> Problem | None:
    solutions = solution_files(directory)
    if not solutions:
        return None

    directory_match = NUMBERED_DIRECTORY.match(directory.name)
    directory_id = int(directory_match.group("id")) if directory_match else None
    directory_slug = directory_match.group("slug") if directory_match else directory.name

    readme_path = directory / "README.md"
    readme = (
        parse_readme(readme_path.read_text(encoding="utf-8")) if readme_path.exists() else {}
    )
    meta = parse_meta_yaml(directory / "meta.yaml")

    raw_id = directory_id if directory_id is not None else readme.get("id", meta.get("id"))
    try:
        problem_id = int(raw_id) if raw_id is not None else None
    except (TypeError, ValueError) as error:
        raise ValueError(f"{directory / 'meta.yaml'}: id must be an integer") from error

    slug = str(readme.get("slug") or meta.get("slug") or directory_slug).strip().strip("/")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug):
        raise ValueError(f"{directory}: invalid problem slug {slug!r}")
    title = str(readme.get("title") or meta.get("title") or slug.replace("-", " ").title())

    readme_difficulty = readme.get("difficulty")
    difficulty = normalize_difficulty(
        readme_difficulty if readme_difficulty is not None else meta.get("difficulty")
    )
    readme_topics = readme.get("topics")
    topics = topics_from(readme_topics if readme_topics else meta.get("topics"))
    languages = tuple(
        sorted({LANGUAGE_BY_SUFFIX[path.suffix.lower()] for path in solutions}, key=str.casefold)
    )
    solution_path = (Path(directory.name) / solutions[0].name).as_posix()
    tested = (directory / "tests.py").is_file() or (directory / "tests_cpp.cpp").is_file()
    return Problem(
        id=problem_id,
        slug=slug,
        title=title,
        difficulty=difficulty,
        topics=topics,
        languages=languages,
        path=directory.name,
        url=f"https://leetcode.com/problems/{slug}/",
        solution_path=solution_path,
        tested=tested,
    )


def discover_problems(root: Path) -> list[Problem]:
    problems: list[Problem] = []
    for directory in sorted(root.iterdir(), key=lambda path: path.name.casefold()):
        if (
            not directory.is_dir()
            or directory.name.startswith(".")
            or directory.name in IGNORED_DIRECTORIES
        ):
            continue
        problem = problem_from_directory(directory)
        if problem is not None:
            problems.append(problem)
    return sorted(
        problems,
        key=lambda problem: (
            problem.id is None,
            problem.id if problem.id is not None else 0,
            problem.slug.casefold(),
        ),
    )


def counts_for(problems: list[Problem]) -> dict[str, int]:
    counts = {"easy": 0, "medium": 0, "hard": 0, "total": len(problems)}
    for problem in problems:
        key = problem.difficulty.lower()
        if key in {"easy", "medium", "hard"}:
            counts[key] += 1
    return counts


def generated_time() -> str:
    source_epoch = os.environ.get("SOURCE_DATE_EPOCH")
    if source_epoch is not None:
        try:
            moment = datetime.fromtimestamp(int(source_epoch), tz=timezone.utc)
        except (ValueError, OverflowError) as error:
            raise ValueError("SOURCE_DATE_EPOCH must be an integer Unix timestamp") from error
    else:
        moment = datetime.now(timezone.utc)
    return moment.replace(microsecond=0).isoformat().replace("+00:00", "Z")


def build_manifest(root: Path, problems: list[Problem]) -> dict[str, object]:
    counts = counts_for(problems)
    problem_data = [problem.as_json() for problem in problems]
    generated = None
    manifest_path = root / "problems.json"
    if manifest_path.exists():
        try:
            existing = json.loads(manifest_path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            existing = None
        if (
            isinstance(existing, dict)
            and existing.get("counts") == counts
            and existing.get("problems") == problem_data
            and isinstance(existing.get("generated"), str)
        ):
            generated = existing["generated"]
    return {
        "generated": generated or generated_time(),
        "counts": counts,
        "problems": problem_data,
    }


def escape_cell(value: object) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ")


def render_index(problems: list[Problem], counts: dict[str, int]) -> str:
    lines = [
        f"**Solved:** {counts['total']} total | {counts['easy']} easy | "
        f"{counts['medium']} medium | {counts['hard']} hard",
        "",
        "| # | Title | Difficulty | Topics | Language |",
        "| ---: | --- | --- | --- | --- |",
    ]
    for problem in problems:
        number = problem.id if problem.id is not None else "-"
        link = quote(problem.solution_path, safe="/._-")
        title = f"[{escape_cell(problem.title)}]({link})"
        topics = ", ".join(escape_cell(topic) for topic in problem.topics) or "-"
        languages = ", ".join(problem.languages)
        if not problem.tested:
            languages += " (untested)"
        lines.append(
            f"| {number} | {title} | {problem.difficulty} | {topics} | {languages} |"
        )
    return "\n".join(lines)


def rewrite_readme(readme: str, index: str) -> str:
    pattern = re.compile(
        rf"{re.escape(INDEX_BEGIN)}.*?{re.escape(INDEX_END)}", re.DOTALL
    )
    if len(pattern.findall(readme)) != 1:
        raise ValueError("README.md must contain exactly one INDEX:BEGIN/INDEX:END block")
    return pattern.sub(f"{INDEX_BEGIN}\n{index}\n{INDEX_END}", readme)


def serialized_manifest(manifest: dict[str, object]) -> str:
    return json.dumps(manifest, indent=2, ensure_ascii=False) + "\n"


def differs(path: Path, expected: str) -> bool:
    try:
        return path.read_text(encoding="utf-8") != expected
    except FileNotFoundError:
        return True


def generate(root: Path, check: bool) -> int:
    readme_path = root / "README.md"
    if not readme_path.is_file():
        raise ValueError(f"README.md not found under {root}")

    problems = discover_problems(root)
    manifest = build_manifest(root, problems)
    expected_manifest = serialized_manifest(manifest)
    expected_readme = rewrite_readme(
        readme_path.read_text(encoding="utf-8"),
        render_index(problems, manifest["counts"]),  # type: ignore[arg-type]
    )

    stale = [
        path
        for path, expected in (
            (readme_path, expected_readme),
            (root / "problems.json", expected_manifest),
        )
        if differs(path, expected)
    ]
    if check:
        if stale:
            names = ", ".join(path.name for path in stale)
            print(
                f"Stale generated files: {names}. Run tools/generate_index.py.",
                file=sys.stderr,
            )
            return 1
        print("README.md and problems.json are current.")
        return 0

    if readme_path in stale:
        readme_path.write_text(expected_readme, encoding="utf-8")
    manifest_path = root / "problems.json"
    if manifest_path in stale:
        manifest_path.write_text(expected_manifest, encoding="utf-8")
    if stale:
        print("Updated " + ", ".join(path.name for path in stale) + ".")
    else:
        print("README.md and problems.json are already current.")
    return 0


def parse_args(arguments: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail instead of writing stale files")
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help=argparse.SUPPRESS,
    )
    return parser.parse_args(arguments)


def main(arguments: list[str] | None = None) -> int:
    args = parse_args(arguments)
    try:
        return generate(args.root.resolve(), args.check)
    except (OSError, ValueError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
