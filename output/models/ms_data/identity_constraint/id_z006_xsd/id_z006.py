from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class CType:
    class Meta:
        name = "cType"

    att_c: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class CsType:
    class Meta:
        name = "csType"

    c: None | CType = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class BType:
    class Meta:
        name = "bType"

    cs: list[CsType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 11,
        },
    )
    att_b: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class BsType:
    class Meta:
        name = "bsType"

    b: list[BType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 11,
        },
    )


@dataclass(kw_only=True)
class AType:
    class Meta:
        name = "aType"

    bs: list[BsType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 11,
        },
    )
    cs: None | CsType = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    att_a: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(kw_only=True)
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


@dataclass(kw_only=True)
class Root(RType):
    class Meta:
        name = "root"
