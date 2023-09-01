"""App contexts."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .models import Temp

if TYPE_CHECKING:
    from django.http import HttpRequest


def temp_context(
    request: HttpRequest | None,  # noqa: ARG001
) -> dict[str, Any]:
    """Temp context."""
    temp = Temp()
    return {
        "temp": str(temp),
    }
