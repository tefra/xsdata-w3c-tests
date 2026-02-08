from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "foo"


@dataclass(kw_only=True)
class A:
    class Meta:
        name = "a"
        namespace = "foo"

    value: str = field(
        default="",
        metadata={
            "pattern": r"[b|c]+",
        },
    )
