from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "ElemDecl/abstract"


@dataclass(kw_only=True)
class HeadType:
    ear: None | object = field(
        default=None,
        metadata={
            "name": "Ear",
            "type": "Element",
            "namespace": "ElemDecl/abstract",
        },
    )
    eye: None | object = field(
        default=None,
        metadata={
            "name": "Eye",
            "type": "Element",
            "namespace": "ElemDecl/abstract",
        },
    )


@dataclass(kw_only=True)
class Head(HeadType):
    class Meta:
        namespace = "ElemDecl/abstract"


@dataclass(kw_only=True)
class Member1(HeadType):
    class Meta:
        namespace = "ElemDecl/abstract"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/abstract"

    member1: list[Member1] = field(
        default_factory=list,
        metadata={
            "name": "Member1",
            "type": "Element",
        },
    )
