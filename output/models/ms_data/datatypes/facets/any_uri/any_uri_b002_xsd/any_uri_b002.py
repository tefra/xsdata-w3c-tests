from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class St(Enum):
    X_Y = "xあy"
    A_B = "a名前空間名前空間名前空間名前空間名前空間名前空間名前空間名前空間名前空間名前空間名前空間名前空間名前空間b"
    ANY_URI_C = "anyURI:c"


@dataclass(kw_only=True)
class Ct:
    class Meta:
        name = "ct"

    value: St = field()
    att: None | St = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Bar(Ct):
    class Meta:
        name = "bar"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    bar: list[Bar] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 100,
        },
    )
