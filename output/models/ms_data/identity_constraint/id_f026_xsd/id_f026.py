from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Rtype:
    class Meta:
        name = "rtype"

    value: str = field(default="")
    val: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class R(Rtype):
    class Meta:
        name = "r"


@dataclass(kw_only=True)
class R2(Rtype):
    class Meta:
        name = "r2"


@dataclass(kw_only=True)
class T:
    class Meta:
        name = "t"

    r2_or_r: None | R2 | R = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "r2",
                    "type": R2,
                },
                {
                    "name": "r",
                    "type": R,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    t: list[T] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
