from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "myNS.tempuri.org"


@dataclass
class ParentType:
    class Meta:
        name = "parentType"


@dataclass
class Ttype:
    class Meta:
        name = "ttype"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    col: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "myNS.tempuri.org",
        },
    )


@dataclass
class T(Ttype):
    class Meta:
        name = "t"
        namespace = "myNS.tempuri.org"


@dataclass
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
