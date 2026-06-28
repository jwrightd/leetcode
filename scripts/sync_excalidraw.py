#!/usr/bin/env python3
"""Copy Excalidraw exports from an inbox into matching LeetCode folders."""

from __future__ import annotations

import argparse
import re
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path


SUPPORTED_SUFFIXES = (
    ".excalidraw.png",
    ".excalidraw.svg",
    ".excalidraw",
    ".png",
    ".svg",
)


@dataclass(frozen=True)
class ProblemDir:
    path: Path
    number: str
    slug: str


def normalize_slug(value: str) -> str:
    value = value.lower().strip()
    value = re.sub(r"[\s_]+", "-", value)
    value = re.sub(r"[^a-z0-9-]", "", value)
    value = re.sub(r"-+", "-", value)
    return value.strip("-")


def drawing_suffix(path: Path) -> str | None:
    lower_name = path.name.lower()
    for suffix in SUPPORTED_SUFFIXES:
        if lower_name.endswith(suffix):
            return suffix
    return None


def drawing_stem(path: Path, suffix: str) -> str:
    return path.name[: -len(suffix)]


def problem_dirs(repo_root: Path) -> list[ProblemDir]:
    problems: list[ProblemDir] = []
    for child in repo_root.iterdir():
        if not child.is_dir():
            continue
        match = re.match(r"^(\d+)-(.+)$", child.name)
        if not match:
            continue
        problems.append(
            ProblemDir(
                path=child,
                number=match.group(1),
                slug=normalize_slug(match.group(2)),
            )
        )
    return sorted(problems, key=lambda problem: problem.path.name)


def lookup_problem(stem: str, problems: list[ProblemDir]) -> ProblemDir | None:
    normalized = normalize_slug(stem)
    by_number = {problem.number.lstrip("0") or "0": problem for problem in problems}
    by_number.update({problem.number: problem for problem in problems})
    by_slug = {problem.slug: problem for problem in problems}

    numeric_match = re.match(r"^0*(\d+)(?:-|$)", normalized)
    if numeric_match:
        problem = by_number.get(numeric_match.group(1))
        if problem is not None:
            return problem

    if normalized in by_slug:
        return by_slug[normalized]

    without_number = re.sub(r"^0*\d+-", "", normalized)
    return by_slug.get(without_number)


def iter_drawings(inbox: Path) -> list[tuple[Path, str]]:
    if not inbox.exists():
        return []

    drawings: list[tuple[Path, str]] = []
    for path in sorted(inbox.iterdir()):
        if not path.is_file():
            continue
        suffix = drawing_suffix(path)
        if suffix is not None:
            drawings.append((path, suffix))
    return drawings


def copy_drawing(
    source: Path,
    suffix: str,
    problem: ProblemDir,
    dest_name: str | None,
    dry_run: bool,
) -> str:
    target_name = dest_name if dest_name is not None else source.name
    if dest_name is not None and not target_name.lower().endswith(suffix):
        target_name = f"{target_name}{suffix}"

    target = problem.path / target_name

    if dry_run:
        return f"would copy {source} -> {target}"

    shutil.copy2(source, target)
    return f"copied {source} -> {target}"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Copy Excalidraw files into matching LeetCode solution folders."
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Repository root. Defaults to this script's parent repo.",
    )
    parser.add_argument(
        "--inbox",
        type=Path,
        default=None,
        help="Folder containing Excalidraw exports. Defaults to <repo>/excalidraw-inbox.",
    )
    parser.add_argument(
        "--dest-name",
        default=None,
        help="Optional destination file name to use inside every matched problem folder.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be copied without writing files.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo_root = args.repo_root.resolve()
    inbox = (args.inbox or repo_root / "excalidraw-inbox").resolve()
    problems = problem_dirs(repo_root)

    if not problems:
        print(f"No LeetCode problem folders found in {repo_root}", file=sys.stderr)
        return 1

    drawings = iter_drawings(inbox)
    if not drawings:
        print(f"No supported Excalidraw files found in {inbox}")
        return 0

    unmatched: list[Path] = []
    copied = 0

    for source, suffix in drawings:
        stem = drawing_stem(source, suffix)
        problem = lookup_problem(stem, problems)
        if problem is None:
            unmatched.append(source)
            continue

        print(copy_drawing(source, suffix, problem, args.dest_name, args.dry_run))
        copied += 1

    if unmatched:
        print("\nUnmatched drawings:", file=sys.stderr)
        for source in unmatched:
            print(f"  {source}", file=sys.stderr)
        print(
            "Name each file with a problem number or slug, like 1.excalidraw or 0001-two-sum.excalidraw.",
            file=sys.stderr,
        )

    if args.dry_run:
        print(f"\nMatched {copied} drawing(s). No files were copied.")
    else:
        print(f"\nCopied {copied} drawing(s).")

    return 1 if unmatched else 0


if __name__ == "__main__":
    raise SystemExit(main())
