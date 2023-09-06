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
    with Path.open(path, "rb") as file:
        content = file.read()

    content = content.replace(b"\r\n", b"\n")

    with Path.open(path, "wb") as file:
        file.write(content)


def yamlfix_cli() -> None:
    """Call yamlfix from cli and exclude .gitignore paths."""
    paths_gitignore = filter_file_lines(read_file_lines(".gitignore"))
    exclude = format_paths_exclude(paths_gitignore)
    yaml_files = filter_yaml_files(find_yaml_files(), paths_gitignore)
    subprocess.run(
        f"poetry run yamlfix . --exclude={exclude}",  # noqa: S603
        check=False,
    )
    for yaml_file in yaml_files:
        fix_yaml_file_endings(yaml_file)


yamlfix_cli()
