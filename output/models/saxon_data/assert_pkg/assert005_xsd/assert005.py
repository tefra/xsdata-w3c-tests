from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Inner:
    class Meta:
        name = "inner"

    a: list[Inner.A] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 4,
        },
    )
    x: object = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    y: None | object = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass(kw_only=True)
    class A:
        b: list[object] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "max_occurs": 4,
            },
        )


@dataclass(kw_only=True)
class Outer:
    class Meta:
        name = "outer"

    inner: list[Inner] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
