from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "systemId"


@dataclass(kw_only=True)
class A:
    class Meta:
        name = "a"
        namespace = "systemId"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
