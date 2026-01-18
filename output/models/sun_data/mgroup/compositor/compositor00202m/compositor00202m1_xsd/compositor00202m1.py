from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "compositor"


@dataclass(kw_only=True)
class A:
    class Meta:
        name = "a"
        namespace = "compositor"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class B:
    class Meta:
        name = "b"
        namespace = "compositor"
