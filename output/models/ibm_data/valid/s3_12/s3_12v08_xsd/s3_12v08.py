from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

__NAMESPACE__ = "tns"


@dataclass(kw_only=True)
class ChildType:
    class Meta:
        name = "childType"

    type1: None | bool = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    type2: None | bool = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DerivedType1(ChildType):
    class Meta:
        name = "derivedType1"

    content: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    value: bool = field()


@dataclass(kw_only=True)
class DerivedType2(ChildType):
    class Meta:
        name = "derivedType2"

    content: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    value: int = field()


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "tns"

    child: list[ChildType | DerivedType1 | DerivedType2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
