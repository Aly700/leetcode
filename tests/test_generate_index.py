import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
GENERATOR = REPO_ROOT / "tools" / "generate_index.py"


class GenerateIndexTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.repo = Path(self.temp_dir.name)
        (self.repo / "README.md").write_text(
            "# leetcode\n\n<!-- INDEX:BEGIN -->\nold index\n<!-- INDEX:END -->\n",
            encoding="utf-8",
        )

    def tearDown(self):
        self.temp_dir.cleanup()

    def run_generator(self, *arguments: str, epoch: int = 0):
        environment = os.environ.copy()
        environment["SOURCE_DATE_EPOCH"] = str(epoch)
        return subprocess.run(
            [sys.executable, str(GENERATOR), "--root", str(self.repo), *arguments],
            text=True,
            capture_output=True,
            env=environment,
            check=False,
        )

    def add_fixture_problems(self):
        numbered = self.repo / "0347-top-k-frequent-elements"
        numbered.mkdir()
        (numbered / "0347-top-k-frequent-elements.py").write_text(
            "class Solution:\n    pass\n", encoding="utf-8"
        )
        (numbered / "tests.py").write_text("def run(solution):\n    pass\n", encoding="utf-8")
        (numbered / "README.md").write_text(
            '<h2><a href="https://leetcode.com/problems/top-k-frequent-elements/">'
            "347. Top K Frequent Elements</a></h2><h3>Medium</h3>\n"
            "<!---LeetCode Topics Start-->\n"
            "# LeetCode Topics\n## Array\n## Hash Table\n## Heap (Priority Queue)\n"
            "<!---LeetCode Topics End-->\n",
            encoding="utf-8",
        )
        (numbered / "meta.yaml").write_text(
            "difficulty: Hard\ntopics: [Ignored Topic]\n", encoding="utf-8"
        )

        plain = self.repo / "binary-tree-paths"
        plain.mkdir()
        (plain / "solution.cpp").write_text("class Solution {};\n", encoding="utf-8")
        (plain / "tests_cpp.cpp").write_text("int main() { return 0; }\n", encoding="utf-8")
        (plain / "README.md").write_text(
            "# [257. Binary Tree Paths](https://leetcode.com/problems/binary-tree-paths/)\n",
            encoding="utf-8",
        )
        (plain / "meta.yaml").write_text(
            "difficulty: Easy\n"
            "topics:\n"
            "  - Tree\n"
            "  - Depth-First Search\n",
            encoding="utf-8",
        )

        untested = self.repo / "plain-slug"
        untested.mkdir()
        (untested / "answer.js").write_text("const answer = 1;\n", encoding="utf-8")

        ignored = self.repo / "notes"
        ignored.mkdir()
        (ignored / "README.md").write_text("not a solution\n", encoding="utf-8")

        infrastructure = self.repo / "tests"
        infrastructure.mkdir()
        (infrastructure / "test_tools.py").write_text("assert True\n", encoding="utf-8")

    def test_generates_manifest_and_marked_readme_index(self):
        self.add_fixture_problems()

        result = self.run_generator()

        self.assertEqual(result.returncode, 0, result.stderr)
        manifest = json.loads((self.repo / "problems.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["generated"], "1970-01-01T00:00:00Z")
        self.assertEqual(
            manifest["counts"],
            {"easy": 1, "medium": 1, "hard": 0, "total": 3},
        )
        self.assertEqual([item["id"] for item in manifest["problems"]], [257, 347, None])
        self.assertEqual(
            manifest["problems"][0],
            {
                "id": 257,
                "slug": "binary-tree-paths",
                "title": "Binary Tree Paths",
                "difficulty": "Easy",
                "topics": ["Tree", "Depth-First Search"],
                "languages": ["C++"],
                "path": "binary-tree-paths",
                "url": "https://leetcode.com/problems/binary-tree-paths/",
            },
        )
        self.assertEqual(manifest["problems"][1]["difficulty"], "Medium")
        self.assertEqual(
            manifest["problems"][1]["topics"],
            ["Array", "Hash Table", "Heap (Priority Queue)"],
        )
        readme = (self.repo / "README.md").read_text(encoding="utf-8")
        self.assertIn("3 total | 1 easy | 1 medium | 0 hard", readme)
        self.assertIn(
            "[Binary Tree Paths](binary-tree-paths/solution.cpp) | Easy | "
            "Tree, Depth-First Search | C++",
            readme,
        )
        self.assertIn(
            "[Top K Frequent Elements](0347-top-k-frequent-elements/0347-top-k-frequent-elements.py)",
            readme,
        )
        self.assertIn(
            "[Plain Slug](plain-slug/answer.js) | Unknown | - | JavaScript (untested)",
            readme,
        )

    def test_repeated_generation_preserves_timestamp_and_bytes(self):
        self.add_fixture_problems()
        first = self.run_generator(epoch=10)
        self.assertEqual(first.returncode, 0, first.stderr)
        first_manifest = (self.repo / "problems.json").read_bytes()
        first_readme = (self.repo / "README.md").read_bytes()

        second = self.run_generator(epoch=999)

        self.assertEqual(second.returncode, 0, second.stderr)
        self.assertEqual((self.repo / "problems.json").read_bytes(), first_manifest)
        self.assertEqual((self.repo / "README.md").read_bytes(), first_readme)

    def test_check_reports_stale_files_without_rewriting_them(self):
        self.add_fixture_problems()
        generated = self.run_generator()
        self.assertEqual(generated.returncode, 0, generated.stderr)
        readme_before = (self.repo / "README.md").read_bytes()
        manifest_before = (self.repo / "problems.json").read_bytes()
        problem = self.repo / "0347-top-k-frequent-elements"
        (problem / "extra.rs").write_text("fn main() {}\n", encoding="utf-8")

        checked = self.run_generator("--check", epoch=20)

        self.assertNotEqual(checked.returncode, 0)
        self.assertIn("problems.json", checked.stderr)
        self.assertIn("README.md", checked.stderr)
        self.assertEqual((self.repo / "README.md").read_bytes(), readme_before)
        self.assertEqual((self.repo / "problems.json").read_bytes(), manifest_before)


if __name__ == "__main__":
    unittest.main()
