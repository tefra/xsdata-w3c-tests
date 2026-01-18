from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class R:
    class Meta:
        name = "r"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class R2:
    class Meta:
        name = "r2"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class Rtype:
    class Meta:
        name = "rtype"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    val: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


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
