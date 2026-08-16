"""Shared path helpers for the drama suite tests.

Upstream, the suite root was the repository root and the nine sibling skills
lived under a `skills/` subdirectory. In this repository the suite root is the
`drama` category directory (`skills/drama/`), with the nine skills directly
under it and the suite's own infrastructure (`tools/`, `tests/`, `demo/`)
sitting beside them. These helpers hide that difference from the tests.
"""

from __future__ import annotations

import shutil
from pathlib import Path

# Repo contract files this repository adds inside every skill directory. They
# are exempt from the suite byte inventory (see the noise sets in
# suite_verify.py / update_suite_manifest.py) and from the "no URLs / no
# private vocabulary in shipped content" scans, because provenance.yaml must
# name the upstream source repository.
REPO_METADATA_NAMES = frozenset(
    {"manifest.yaml", "README.md", "provenance.yaml", "LICENSE", "cases.yaml"}
)


def suite_root() -> Path:
    return Path(__file__).resolve().parents[1]


def skill_dirs(root: Path | None = None) -> list[Path]:
    """The nine sibling skills directly under the suite root."""
    root = root or suite_root()
    return sorted(path for path in root.iterdir() if (path / "SKILL.md").is_file())


def is_shipped_content(path: Path, root: Path | None = None) -> bool:
    """True for a file inside one of the nine skills that is not repo metadata."""
    root = root or suite_root()
    parts = path.relative_to(root).parts
    if not parts:
        return False
    if not (root / parts[0] / "SKILL.md").is_file():
        # demo/, tools/ and tests/ live beside the skills, not inside them.
        return False
    return parts[-1] not in REPO_METADATA_NAMES


def copy_skills(source: Path, destination: Path) -> None:
    """Copy only the sibling skill directories, never the suite's own infra."""
    for skill in skill_dirs(source):
        shutil.copytree(
            skill,
            destination / skill.name,
            ignore=shutil.ignore_patterns("__pycache__", "*.pyc"),
        )
