#!/usr/bin/env python3
"""Build the repository index from Skill and Pack manifests."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]


def load_yaml(path: Path) -> dict:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return data


def required(data: dict, key: str, path: Path):
    if key not in data:
        raise ValueError(f"{path}: missing {key}")
    return data[key]


def registry_data(root: Path) -> dict:
    skills = []
    for manifest_path in sorted((root / "skills").glob("*/*/manifest.yaml")):
        manifest = load_yaml(manifest_path)
        skill_dir = manifest_path.parent
        skills.append(
            {
                "id": required(manifest, "id", manifest_path),
                "name": required(manifest, "name", manifest_path),
                "version": required(manifest, "version", manifest_path),
                "status": required(manifest, "status", manifest_path),
                "path": skill_dir.relative_to(root).as_posix(),
                "entrypoint": required(manifest, "entrypoint", manifest_path),
                "tags": manifest.get("tags", []),
            }
        )

    packs = []
    for pack_path in sorted((root / "packs").glob("*/pack.yaml")):
        pack = load_yaml(pack_path)
        packs.append(
            {
                "id": required(pack, "id", pack_path),
                "name": required(pack, "name", pack_path),
                "version": required(pack, "version", pack_path),
                "path": pack_path.parent.relative_to(root).as_posix(),
            }
        )

    return {
        "schema_version": 1,
        "generated_from": ["skills", "packs"],
        "skills": sorted(skills, key=lambda item: item["id"]),
        "packs": sorted(packs, key=lambda item: item["id"]),
    }


def render_registry(root: Path) -> str:
    return yaml.safe_dump(
        registry_data(root), sort_keys=False, allow_unicode=True, width=100
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="fail if registry.yaml is stale")
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    registry_path = args.root / "registry.yaml"

    try:
        expected = render_registry(args.root)
        if args.check:
            actual = registry_path.read_text(encoding="utf-8") if registry_path.exists() else ""
            if actual != expected:
                print("registry.yaml is stale; run python tools/build_registry.py", file=sys.stderr)
                return 1
            print("registry.yaml is current")
            return 0

        registry_path.write_text(expected, encoding="utf-8")
        print(f"wrote {registry_path.relative_to(args.root)}")
        return 0
    except (OSError, ValueError, KeyError, yaml.YAMLError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
