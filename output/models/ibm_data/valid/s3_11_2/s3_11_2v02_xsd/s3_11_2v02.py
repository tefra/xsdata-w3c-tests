from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "a"


@dataclass(kw_only=True)
class Numtype:
    class Meta:
        name = "numtype"

    value: int = field()
    id_1: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    id_2: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "a"

    number: list[Numtype] = field(
        default_factory=list,
        metadata={
            "name": "Number",
            "type": "Element",
            "min_occurs": 1,
        },
    )
