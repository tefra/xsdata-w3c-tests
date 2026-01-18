from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://test2"


@dataclass(kw_only=True)
class A:
    class Meta:
        name = "a"
        namespace = "http://test2"

    value: int = field()


@dataclass(kw_only=True)
class Y:
    class Meta:
        name = "y"
        namespace = "http://test2"

    a: list[A] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
