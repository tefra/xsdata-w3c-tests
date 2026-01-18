from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "ElemDecl/substGroupExclusions"


@dataclass(kw_only=True)
class HeadType:
    ear: None | object = field(
        default=None,
        metadata={
            "name": "Ear",
            "type": "Element",
            "namespace": "ElemDecl/substGroupExclusions",
        },
    )
    eye: None | object = field(
        default=None,
        metadata={
            "name": "Eye",
            "type": "Element",
            "namespace": "ElemDecl/substGroupExclusions",
        },
    )


@dataclass(kw_only=True)
class Head(HeadType):
    class Meta:
        namespace = "ElemDecl/substGroupExclusions"


@dataclass(kw_only=True)
class Member3(HeadType):
    class Meta:
        namespace = "ElemDecl/substGroupExclusions"

    nose: None | object = field(
        default=None,
        metadata={
            "name": "Nose",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/substGroupExclusions"

    head: list[Head] = field(
        default_factory=list,
        metadata={
            "name": "Head",
            "type": "Element",
            "min_occurs": 1,
        },
    )
