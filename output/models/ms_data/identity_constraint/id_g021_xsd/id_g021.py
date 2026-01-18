from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "myNS.tempuri.org"


@dataclass(kw_only=True)
class T:
    class Meta:
        name = "t"
        namespace = "myNS.tempuri.org"

    row: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    col: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "myNS.tempuri.org"

    t: list[T] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
