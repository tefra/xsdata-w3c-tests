from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional


class St(Enum):
    X_Y = "xあy"
    A_B = "a名前空間名前空間名前空間名前空間名前空間名前空間名前空間名前空間名前空間名前空間名前空間名前空間名前空間b"
    ANY_URI_C = "anyURI:c"


@dataclass
class Ct:
    class Meta:
        name = "ct"

    value: Optional[St] = field(
        default=None
    )
    att: Optional[St] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Bar(Ct):
    class Meta:
        name = "bar"


@dataclass
class Root:
    class Meta:
        name = "root"

    bar: List[Bar] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 100,
        }
    )
