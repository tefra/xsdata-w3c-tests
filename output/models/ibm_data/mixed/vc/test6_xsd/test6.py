from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Example:
    value: int = field(
        metadata={
            "required": True,
        }
    )
