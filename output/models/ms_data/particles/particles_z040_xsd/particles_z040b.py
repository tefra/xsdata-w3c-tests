from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "b"


@dataclass(kw_only=True)
class B1:
    class Meta:
        name = "b1"
        namespace = "b"

    value: str = field(
        default="b1",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class B2:
    class Meta:
        name = "b2"
        namespace = "b"

    value: str = field(
        init=False,
        default="b2",
        metadata={
            "required": True,
        },
    )
