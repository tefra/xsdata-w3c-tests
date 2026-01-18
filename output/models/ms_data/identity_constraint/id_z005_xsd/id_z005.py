from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class BType:
    class Meta:
        name = "bType"

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

    b: None | BType = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class AType:
    class Meta:
        name = "aType"

    bs: None | BsType = field(
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
