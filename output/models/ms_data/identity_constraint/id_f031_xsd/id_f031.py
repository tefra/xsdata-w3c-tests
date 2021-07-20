from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class R:
    class Meta:
        name = "r"

    value: Optional[str] = field(
        default=None
    )


@dataclass
class R2:
    class Meta:
        name = "r2"

    value: Optional[str] = field(
        default=None
    )


@dataclass
class Rtype:
    class Meta:
        name = "rtype"

    value: Optional[str] = field(
        default=None
    )
    val: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class T:
    class Meta:
        name = "t"

    r2: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    r: Optional[str] = field(
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
