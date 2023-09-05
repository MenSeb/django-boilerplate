"""Fix linting errors from YAML files and exclude .gitignore paths."""


from __future__ import annotations

import subprocess
from pathlib import Path


def read_file_lines(path: str) -> list[str]:
    """Read the lines from a file."""
    return Path.open(path).read().split("\n")


def is_empty_or_comment(line: str) -> bool:
    """Return true if not an empty line or comment."""
    return not (line.startswith("#") or line == "")


def filter_file_lines(lines: list[str]) -> list[str]:
    """Filter the comments and empty lines from a file."""
    return list(filter(is_empty_or_comment, lines))


def format_path_glob(path: str) -> str:
    """Format a path with glob /**/* if path is a folder."""
    return f"{path}**/*" if path.endswith("/") else path


def format_paths_exclude(paths: list[str]) -> str:
    """Extract paths from .gitignore file."""
    return " --exclude=".join(map(format_path_glob, paths))


def yamlfix_cli() -> None:
    """Call yamlfix from cli and exclude .gitignore paths."""
    exclude = format_paths_exclude(filter_file_lines(read_file_lines(".gitignore")))
    subprocess.run(
        f"poetry run yamlfix . --exclude={exclude}",  # noqa: S603
        check=False,
    )


yamlfix_cli()
