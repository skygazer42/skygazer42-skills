from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import build_registry  # noqa: E402
import validate_repository  # noqa: E402


MANIFEST = """\
schema_version: 1
id: engineering.review-code
name: Review Code
version: 1.0.0
status: stable
description: Review code changes.
category: engineering
entrypoint: SKILL.md
tags: [review]
contents:
  examples:
  references:
  scripts:
  tests: tests
dependencies:
  skills: []
  commands: []
  environment_variables: []
permissions:
  network: false
  read_files: true
  write_files: false
  execute_commands: false
compatibility:
  adapters: []
evaluation:
  cases: tests/cases.yaml
provenance:
  file: provenance.yaml
"""


class RepositoryToolsTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        skill = self.root / "skills/engineering/review-code"
        (skill / "tests").mkdir(parents=True)
        (self.root / "packs/core").mkdir(parents=True)
        (self.root / "incubator").mkdir()
        (self.root / "templates").mkdir()
        (self.root / "tools").mkdir()
        (skill / "SKILL.md").write_text("# Review Code\n", encoding="utf-8")
        (skill / "manifest.yaml").write_text(MANIFEST, encoding="utf-8")
        (skill / "provenance.yaml").write_text(
            "schema_version: 1\norigin:\n  type: original\nlicense: {}\n", encoding="utf-8"
        )
        (skill / "tests/cases.yaml").write_text(
            "schema_version: 1\ncases:\n  - id: basic\n", encoding="utf-8"
        )
        (self.root / "packs/core/pack.yaml").write_text(
            """\
schema_version: 1
id: pack.core
name: Core
version: 1.0.0
description: Core skills.
skills:
  - id: engineering.review-code
    version: ">=1.0.0 <2.0.0"
""",
            encoding="utf-8",
        )
        (self.root / "registry.yaml").write_text(
            build_registry.render_registry(self.root), encoding="utf-8"
        )

    def tearDown(self) -> None:
        self.temp.cleanup()

    def test_valid_repository(self) -> None:
        self.assertEqual([], validate_repository.validate(self.root))

    def test_unknown_pack_reference_is_rejected(self) -> None:
        pack = self.root / "packs/core/pack.yaml"
        pack.write_text(
            pack.read_text(encoding="utf-8").replace(
                "engineering.review-code", "engineering.missing"
            ),
            encoding="utf-8",
        )
        self.assertTrue(
            any("unknown skill reference" in error for error in validate_repository.validate(self.root))
        )

    def test_high_signal_secret_is_rejected(self) -> None:
        (self.root / "leak.txt").write_text("AKIA" + "A" * 16, encoding="utf-8")
        self.assertTrue(
            any("AWS access key" in error for error in validate_repository.validate(self.root))
        )

    def test_external_skill_needs_exact_provenance(self) -> None:
        (self.root / "skills/engineering/review-code/provenance.yaml").write_text(
            "schema_version: 1\norigin:\n  type: adapted\nlicense: {}\n", encoding="utf-8"
        )
        self.assertTrue(
            any(
                "external origin.revision is required" in error
                for error in validate_repository.validate(self.root)
            )
        )


if __name__ == "__main__":
    unittest.main()
