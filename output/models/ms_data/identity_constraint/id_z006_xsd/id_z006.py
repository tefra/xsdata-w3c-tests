from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class CType:
    class Meta:
        name = "cType"

    att_c: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class CsType:
    class Meta:
        name = "csType"

    c: Optional[CType] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class BType:
    class Meta:
        name = "bType"

    cs: List[CsType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 11,
        },
    )
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

    b: List[BType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 11,
        },
    )


@dataclass
class AType:
    class Meta:
        name = "aType"

    bs: List[BsType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 11,
        },
    )
    cs: Optional[CsType] = field(
        default=None,
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

    a: List[AType] = field(
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
