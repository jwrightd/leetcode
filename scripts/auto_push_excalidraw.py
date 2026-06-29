#!/usr/bin/env python3
"""Commit and push Excalidraw files placed directly in problem folders."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SUPPORTED_SUFFIXES = (
    ".excalidraw.png",
    ".excalidraw.svg",
    ".excalidraw",
    ".png",
    ".svg",
)


def run(args: list[str], check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        args,
        cwd=REPO_ROOT,
        check=check,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )


def is_problem_dir(path: Path) -> bool:
    return path.is_dir() and re.match(r"^\d+-.+", path.name) is not None


def is_drawing(path: Path) -> bool:
    lower_name = path.name.lower()
    return any(lower_name.endswith(suffix) for suffix in SUPPORTED_SUFFIXES)


def relative(path: Path) -> str:
    return str(path.relative_to(REPO_ROOT))


def render_png_previews() -> None:
    renderer = REPO_ROOT / "scripts" / "render_excalidraw_png.js"
    for problem_dir in REPO_ROOT.iterdir():
        if not is_problem_dir(problem_dir):
            continue
        for path in sorted(problem_dir.iterdir()):
            if path.is_file() and path.name.lower().endswith(".excalidraw"):
                output = Path(f"{path}.png")
                if output.exists() and output.stat().st_mtime >= path.stat().st_mtime:
                    continue
                result = run(
                    ["node", str(renderer), str(path), str(output)],
                    check=False,
                )
                print(result.stdout, end="")
                if result.returncode != 0:
                    print(result.stderr, end="", file=sys.stderr)
                    raise subprocess.CalledProcessError(
                        result.returncode,
                        result.args,
                        output=result.stdout,
                        stderr=result.stderr,
                    )


def candidate_files() -> list[str]:
    files: set[str] = set()

    for problem_dir in REPO_ROOT.iterdir():
        if not is_problem_dir(problem_dir):
            continue
        for path in problem_dir.iterdir():
            if path.is_file() and is_drawing(path):
                files.add(relative(path))

    tracked = run(["git", "ls-files", "-z"], check=False)
    for raw_path in tracked.stdout.split("\0"):
        if not raw_path:
            continue
        path = REPO_ROOT / raw_path
        if len(path.parts) >= len(REPO_ROOT.parts) + 2 and is_drawing(path):
            parent = path.parent
            if parent.parent == REPO_ROOT and is_problem_dir(parent):
                files.add(raw_path)

    return sorted(files)


def changed_paths(paths: list[str]) -> list[str]:
    if not paths:
        return []

    status = run(["git", "status", "--porcelain", "-z", "--", *paths])
    entries = status.stdout.split("\0")
    changed: list[str] = []

    for entry in entries:
        if not entry:
            continue
        # Porcelain entries begin with two status chars and a space. Rename
        # records include two paths; staging either path is harmless here.
        changed.append(entry[3:])

    return changed


def all_changed_paths() -> list[str]:
    status = run(["git", "status", "--porcelain", "-z"])
    entries = status.stdout.split("\0")
    return [entry[3:] for entry in entries if entry]


def current_branch() -> str | None:
    result = run(["git", "branch", "--show-current"], check=False)
    branch = result.stdout.strip()
    return branch or None


def main() -> int:
    branch = current_branch()
    if branch is None:
        print("Not on a branch; skipping Excalidraw auto-push.", file=sys.stderr)
        return 1

    render_png_previews()

    candidates = candidate_files()
    drawings_changed = changed_paths(candidates)
    if not drawings_changed:
        print("No Excalidraw drawing changes to push.")
        return 0

    all_changes = set(all_changed_paths())
    drawing_changes = set(drawings_changed)
    unrelated_changes = sorted(all_changes - drawing_changes)

    run(["git", "add", "--all", "--", *drawings_changed])
    diff = run(["git", "diff", "--cached", "--quiet"], check=False)
    if diff.returncode == 0:
        print("No staged Excalidraw drawing changes to push.")
        return 0

    run(["git", "commit", "-m", "Sync Excalidraw notes"])

    if unrelated_changes:
        print("Committed Excalidraw notes.")
        print("Skipping rebase because unrelated local changes are present:")
        for path in unrelated_changes:
            print(f"  {path}")
    else:
        pull = run(["git", "pull", "--rebase", "origin", branch], check=False)
        if pull.returncode != 0:
            print(pull.stdout, end="")
            print(pull.stderr, end="", file=sys.stderr)
            print("Committed Excalidraw notes, but pull --rebase failed.", file=sys.stderr)
            return pull.returncode

    push = run(["git", "push", "origin", branch], check=False)
    print(push.stdout, end="")
    if push.returncode != 0:
        print(push.stderr, end="", file=sys.stderr)
        print("Committed Excalidraw notes, but push failed.", file=sys.stderr)
        return push.returncode

    print("Pushed Excalidraw notes.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
