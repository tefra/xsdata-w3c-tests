from dataclasses import dataclass, field
from typing import Optional


@dataclass
class BType:
    class Meta:
        name = "bType"

    att_b: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class BsType:
    class Meta:
        name = "bsType"

    b: Optional[BType] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class AType:
    class Meta:
        name = "aType"

    bs: Optional[BsType] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    c: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    att_a: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class RType:
    class Meta:
        name = "rType"

    a: list[AType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class Root(RType):
    class Meta:
        name = "root"
