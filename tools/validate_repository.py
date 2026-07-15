#!/usr/bin/env python3
"""Validate the repository's small, platform-neutral Skill protocol."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

import build_registry


ROOT = Path(__file__).resolve().parents[1]
SEMVER = re.compile(
    r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)"
    r"(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?$"
)
IDENTIFIER = re.compile(r"^[a-z0-9]+(?:[.-][a-z0-9]+)*$")
MANIFEST_FIELDS = (
    "schema_version",
    "id",
    "name",
    "version",
    "status",
    "description",
    "category",
    "entrypoint",
    "tags",
    "contents",
    "dependencies",
    "permissions",
    "compatibility",
    "evaluation",
    "provenance",
)
PERMISSIONS = ("network", "read_files", "write_files", "execute_commands")
SECRET_PATTERNS = (
    ("private key", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")),
    ("AWS access key", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("GitHub token", re.compile(r"\bgh[pousr]_[A-Za-z0-9]{36,}\b")),
    ("GitHub token", re.compile(r"\bgithub_pat_[A-Za-z0-9_]{50,}\b")),
    ("OpenAI key", re.compile(r"\bsk-[A-Za-z0-9_-]{32,}\b")),
)


def child_path(base: Path, value: object, label: str, errors: list[str]) -> Path | None:
    if not isinstance(value, str) or not value:
        errors.append(f"{label}: expected a non-empty relative path")
        return None
    candidate = (base / value).resolve()
    try:
        candidate.relative_to(base.resolve())
    except ValueError:
        errors.append(f"{label}: path escapes its directory")
        return None
    return candidate


def read_yaml(path: Path, errors: list[str]) -> dict:
    try:
        return build_registry.load_yaml(path)
    except (OSError, ValueError, yaml.YAMLError) as error:
        errors.append(str(error))
        return {}


def skill_directories(root: Path) -> list[Path]:
    skills_root = root / "skills"
    if not skills_root.is_dir():
        return []
    return sorted(
        skill
        for category in skills_root.iterdir()
        if category.is_dir() and not category.name.startswith(".")
        for skill in category.iterdir()
        if skill.is_dir() and not skill.name.startswith(".")
    )


def pack_directories(root: Path) -> list[Path]:
    packs_root = root / "packs"
    if not packs_root.is_dir():
        return []
    return sorted(
        path for path in packs_root.iterdir() if path.is_dir() and not path.name.startswith(".")
    )


def has_value(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip()) and not value.startswith("<")


def validate_skill(
    skill_dir: Path,
    errors: list[str],
    identifiers: dict[str, Path],
) -> tuple[str | None, list[str]]:
    label = skill_dir.as_posix()
    entrypoint = skill_dir / "SKILL.md"
    manifest_path = skill_dir / "manifest.yaml"
    if not entrypoint.is_file():
        errors.append(f"{label}: missing SKILL.md")
    if not manifest_path.is_file():
        errors.append(f"{label}: missing manifest.yaml")
        return None, []

    manifest = read_yaml(manifest_path, errors)
    for field in MANIFEST_FIELDS:
        if field not in manifest:
            errors.append(f"{manifest_path}: missing {field}")
    if manifest.get("schema_version") != 1:
        errors.append(f"{manifest_path}: schema_version must be 1")

    skill_id = manifest.get("id")
    if not isinstance(skill_id, str) or not IDENTIFIER.fullmatch(skill_id):
        errors.append(f"{manifest_path}: invalid id")
        skill_id = None
    elif skill_id in identifiers:
        errors.append(f"{manifest_path}: duplicate id {skill_id} (also in {identifiers[skill_id]})")
    else:
        identifiers[skill_id] = manifest_path

    if manifest.get("category") != skill_dir.parent.name:
        errors.append(f"{manifest_path}: category must match directory {skill_dir.parent.name}")
    if not has_value(manifest.get("name")) or not has_value(manifest.get("description")):
        errors.append(f"{manifest_path}: name and description must be non-empty")
    if not isinstance(manifest.get("version"), str) or not SEMVER.fullmatch(manifest["version"]):
        errors.append(f"{manifest_path}: version must use semantic versioning")
    if not isinstance(manifest.get("tags"), list) or not all(
        isinstance(tag, str) for tag in manifest.get("tags", [])
    ):
        errors.append(f"{manifest_path}: tags must be a list of strings")

    declared_entrypoint = child_path(
        skill_dir, manifest.get("entrypoint"), f"{manifest_path}: entrypoint", errors
    )
    if declared_entrypoint and not declared_entrypoint.is_file():
        errors.append(f"{manifest_path}: entrypoint does not exist")

    contents = manifest.get("contents")
    if not isinstance(contents, dict):
        errors.append(f"{manifest_path}: contents must be a mapping")
    else:
        for name, value in contents.items():
            if value is None:
                continue
            directory = child_path(skill_dir, value, f"{manifest_path}: contents.{name}", errors)
            if directory and not directory.is_dir():
                errors.append(f"{manifest_path}: contents.{name} does not exist")

    dependencies = manifest.get("dependencies")
    dependency_ids: list[str] = []
    if not isinstance(dependencies, dict):
        errors.append(f"{manifest_path}: dependencies must be a mapping")
    else:
        for field in ("skills", "commands", "environment_variables"):
            values = dependencies.get(field)
            if not isinstance(values, list) or not all(isinstance(value, str) for value in values):
                errors.append(f"{manifest_path}: dependencies.{field} must be a list of strings")
            elif field == "skills":
                dependency_ids = values

    permissions = manifest.get("permissions")
    if not isinstance(permissions, dict):
        errors.append(f"{manifest_path}: permissions must be a mapping")
    else:
        for permission in PERMISSIONS:
            if not isinstance(permissions.get(permission), bool):
                errors.append(f"{manifest_path}: permissions.{permission} must be boolean")

    compatibility = manifest.get("compatibility")
    if not isinstance(compatibility, dict) or not isinstance(compatibility.get("adapters"), list):
        errors.append(f"{manifest_path}: compatibility.adapters must be a list")

    provenance = manifest.get("provenance")
    provenance_path = None
    if isinstance(provenance, dict):
        provenance_path = child_path(
            skill_dir, provenance.get("file"), f"{manifest_path}: provenance.file", errors
        )
    else:
        errors.append(f"{manifest_path}: provenance must be a mapping")
    if provenance_path and not provenance_path.is_file():
        errors.append(f"{manifest_path}: provenance file does not exist")
    elif provenance_path:
        provenance_data = read_yaml(provenance_path, errors)
        origin = provenance_data.get("origin")
        license_data = provenance_data.get("license")
        if provenance_data.get("schema_version") != 1 or not isinstance(origin, dict):
            errors.append(f"{provenance_path}: invalid provenance metadata")
        elif origin.get("type") in {"adapted", "external", "imported"}:
            for field in ("repository", "revision", "path", "author"):
                if not has_value(origin.get(field)):
                    errors.append(f"{provenance_path}: external origin.{field} is required")
            if not isinstance(license_data, dict):
                errors.append(f"{provenance_path}: external license metadata is required")
            else:
                for field in ("identifier", "file"):
                    if not has_value(license_data.get(field)):
                        errors.append(f"{provenance_path}: external license.{field} is required")

    evaluation = manifest.get("evaluation")
    cases_path = None
    if isinstance(evaluation, dict):
        cases_path = child_path(
            skill_dir, evaluation.get("cases"), f"{manifest_path}: evaluation.cases", errors
        )
    else:
        errors.append(f"{manifest_path}: evaluation must be a mapping")
    if cases_path and not cases_path.is_file():
        errors.append(f"{manifest_path}: evaluation cases do not exist")
    elif cases_path:
        cases = read_yaml(cases_path, errors)
        if cases.get("schema_version") != 1 or not isinstance(cases.get("cases"), list):
            errors.append(f"{cases_path}: expected schema_version 1 and a cases list")
        elif manifest.get("status") == "stable" and not cases["cases"]:
            errors.append(f"{cases_path}: stable skills need at least one evaluation case")

    return skill_id, dependency_ids


def validate_pack(
    pack_dir: Path,
    errors: list[str],
    identifiers: dict[str, Path],
) -> list[str]:
    pack_path = pack_dir / "pack.yaml"
    if not pack_path.is_file():
        errors.append(f"{pack_dir}: missing pack.yaml")
        return []
    if (pack_dir / "SKILL.md").exists():
        errors.append(f"{pack_dir}: packs must reference skills, not copy SKILL.md")

    pack = read_yaml(pack_path, errors)
    for field in ("schema_version", "id", "name", "version", "description", "skills"):
        if field not in pack:
            errors.append(f"{pack_path}: missing {field}")
    if pack.get("schema_version") != 1:
        errors.append(f"{pack_path}: schema_version must be 1")
    pack_id = pack.get("id")
    if not isinstance(pack_id, str) or not IDENTIFIER.fullmatch(pack_id):
        errors.append(f"{pack_path}: invalid id")
    elif pack_id in identifiers:
        errors.append(f"{pack_path}: duplicate id {pack_id} (also in {identifiers[pack_id]})")
    else:
        identifiers[pack_id] = pack_path
    if not isinstance(pack.get("version"), str) or not SEMVER.fullmatch(pack["version"]):
        errors.append(f"{pack_path}: version must use semantic versioning")

    references: list[str] = []
    skills = pack.get("skills")
    if not isinstance(skills, list):
        errors.append(f"{pack_path}: skills must be a list")
        return references
    for index, reference in enumerate(skills):
        if not isinstance(reference, dict) or not has_value(reference.get("id")) or not has_value(
            reference.get("version")
        ):
            errors.append(f"{pack_path}: skills[{index}] needs id and version")
        else:
            references.append(reference["id"])
    if len(references) != len(set(references)):
        errors.append(f"{pack_path}: duplicate skill reference")
    return references


def validate_incubator(root: Path, errors: list[str]) -> None:
    incubator = root / "incubator"
    if not incubator.is_dir():
        errors.append(f"{incubator}: missing directory")
        return
    for candidate in sorted(path for path in incubator.iterdir() if path.is_dir()):
        source_path = candidate / "source.yaml"
        review_path = candidate / "review.md"
        payload_path = candidate / "candidate"
        for path in (source_path, review_path):
            if not path.is_file():
                errors.append(f"{candidate}: missing {path.name}")
        if not payload_path.is_dir():
            errors.append(f"{candidate}: missing candidate directory")
        if source_path.is_file():
            source = read_yaml(source_path, errors)
            for field in ("repository", "revision", "path", "license", "captured_at"):
                if not has_value(source.get(field)):
                    errors.append(f"{source_path}: {field} is required")


def find_secrets(root: Path, errors: list[str]) -> None:
    ignored = {".git", ".venv", "__pycache__"}
    for path in root.rglob("*"):
        if not path.is_file() or path.is_symlink() or ignored.intersection(path.parts):
            continue
        try:
            if path.stat().st_size > 1_000_000:
                continue
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        for line_number, line in enumerate(text.splitlines(), 1):
            for name, pattern in SECRET_PATTERNS:
                if pattern.search(line):
                    errors.append(f"{path}:{line_number}: possible {name}")


def validate(root: Path) -> list[str]:
    errors: list[str] = []
    for required_dir in ("skills", "packs", "templates", "tools"):
        if not (root / required_dir).is_dir():
            errors.append(f"{root / required_dir}: missing directory")

    identifiers: dict[str, Path] = {}
    skill_dependencies: list[tuple[str, str]] = []
    skill_ids: set[str] = set()
    for skill_dir in skill_directories(root):
        skill_id, dependencies = validate_skill(skill_dir, errors, identifiers)
        if skill_id:
            skill_ids.add(skill_id)
            skill_dependencies.extend((skill_id, dependency) for dependency in dependencies)

    pack_references: list[tuple[Path, str]] = []
    for pack_dir in pack_directories(root):
        pack_references.extend((pack_dir, reference) for reference in validate_pack(pack_dir, errors, identifiers))

    for skill_id, dependency in skill_dependencies:
        if dependency not in skill_ids:
            errors.append(f"{skill_id}: unknown skill dependency {dependency}")
    for pack_dir, reference in pack_references:
        if reference not in skill_ids:
            errors.append(f"{pack_dir}: unknown skill reference {reference}")

    validate_incubator(root, errors)
    find_secrets(root, errors)

    if not errors:
        registry_path = root / "registry.yaml"
        expected = build_registry.render_registry(root)
        actual = registry_path.read_text(encoding="utf-8") if registry_path.is_file() else ""
        if actual != expected:
            errors.append("registry.yaml is stale; run python tools/build_registry.py")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    errors = validate(args.root.resolve())
    if errors:
        for error in errors:
            print(f"error: {error}", file=sys.stderr)
        return 1
    print("repository is valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
