"""Fix linting errors from YAML files and exclude .gitignore paths."""


from __future__ import annotations

import subprocess
from logging import INFO, basicConfig, info
from pathlib import Path
from typing import TextIO

basicConfig(level=INFO)


def read_file_lines(path: str) -> list[str]:
    """Read the lines from a file."""
    return Path.open(path).read().split("\n")


def is_path_folder(line: str) -> bool:
    """Return true if the path is a folder."""
    return line.endswith("/") and not line.startswith("#")


def filter_file_lines(lines: list[str]) -> list[str]:
    """Filter the lines in file to keep the one as folder path."""
    return list(filter(is_path_folder, lines))


def find_yaml_files() -> list[str]:
    """Find YAML files using a glob pattern,."""
    yml = list(map(str, Path().glob("**/*.yml")))
    yaml = list(map(str, Path().glob("**/*.yaml")))
    return yml + yaml


def filter_yaml_file(file: str, paths: list[str]) -> bool:
    """Return true if file starts with one of the paths."""
    return any(file.startswith(path) for path in paths)


def filter_yaml_files(files: list[str], paths: list[str]) -> list[str]:
    """Filter YAML files with paths."""
    str_paths = [str(Path(path)) for path in paths]
    return list(
        filter(lambda file: not filter_yaml_file(file, str_paths), files),
    )


def fix_yaml_file_endings(path: str) -> None:
    """Fix YAML file endings from CRLF to LF."""
    file: TextIO

    with Path.open(path, "rb") as file:
        content = file.read()

    content = content.replace(b"\r\n", b"\n")

    with Path.open(path, "wb") as file:
        file.write(content)

    file.close()


def fix_yaml_files() -> None:
    """Fix all YAML files in the project.

    Find all YAML files in the project excluding paths from .gitignore.

    For each file:
        Call yamlfix cli to fix errors.

        Update line endings from CRLF to LF.
    """
    paths_gitignore = filter_file_lines(read_file_lines(".gitignore"))

    yaml_files = filter_yaml_files(find_yaml_files(), paths_gitignore)

    for yaml_file in yaml_files:
        info(f"YamlFix - File : {yaml_file}")
        subprocess.run(
            f"poetry run yamlfix {yaml_file}",  # noqa: S603
            check=False,
        )
        fix_yaml_file_endings(yaml_file)
