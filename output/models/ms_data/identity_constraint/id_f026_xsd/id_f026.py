from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Rtype:
    class Meta:
        name = "rtype"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    val: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class R(Rtype):
    class Meta:
        name = "r"


@dataclass
class R2(Rtype):
    class Meta:
        name = "r2"


@dataclass
class T:
    class Meta:
        name = "t"

    r2: Optional[R2] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    r: Optional[R] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class Root:
    class Meta:
        name = "root"

    t: List[T] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
