from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Bad:
    class Meta:
        name = "bad"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class Good:
    class Meta:
        name = "good"

    value: int = field(
        metadata={
            "required": True,
        }
    )
