from enum import Enum
from dataclasses import dataclass, field
from typing import List, Optional


class St(Enum):
    """
    :cvar ANY_URI_C:
    :cvar A_B:
    :cvar X_Y:
    """
    ANY_URI_C = "anyURI:c"
    A_B = "a名前空間名前空間名前空間名前空間名前空間名前空間名前空間名前空間名前空間名前空間名前空間名前空間名前空間b"
    X_Y = "xあy"


@dataclass
class Ct:
    """
    :ivar value:
    :ivar att:
    """
    class Meta:
        name = "ct"

    value: Optional[St] = field(
        default=None,
    )
    att: Optional[St] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class Bar(Ct):
    class Meta:
        name = "bar"



@dataclass
class Root:
    """
    :ivar bar:
    """
    class Meta:
        name = "root"

    bar: List[Bar] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=1,
            max_occurs=100
        )
    )
