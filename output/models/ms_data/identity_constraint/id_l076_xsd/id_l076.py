from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "myNS.tempuri.org"


@dataclass(kw_only=True)
class ParentType:
    class Meta:
        name = "parentType"


@dataclass(kw_only=True)
class Ttype:
    class Meta:
        name = "ttype"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    col: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "myNS.tempuri.org",
        },
    )


@dataclass(kw_only=True)
class T(Ttype):
    class Meta:
        name = "t"
        namespace = "myNS.tempuri.org"


@dataclass(kw_only=True)
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
