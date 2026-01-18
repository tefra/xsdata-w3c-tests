from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "ElemDecl/disallowedSubst"


@dataclass(kw_only=True)
class HeadType:
    ear: None | object = field(
        default=None,
        metadata={
            "name": "Ear",
            "type": "Element",
            "namespace": "ElemDecl/disallowedSubst",
        },
    )
    eye: None | object = field(
        default=None,
        metadata={
            "name": "Eye",
            "type": "Element",
            "namespace": "ElemDecl/disallowedSubst",
        },
    )


@dataclass(kw_only=True)
class Head(HeadType):
    class Meta:
        namespace = "ElemDecl/disallowedSubst"


@dataclass(kw_only=True)
class Member1(HeadType):
    class Meta:
        namespace = "ElemDecl/disallowedSubst"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/disallowedSubst"

    member1_or_head: list[Member1 | Head] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "Member1",
                    "type": Member1,
                },
                {
                    "name": "Head",
                    "type": Head,
                },
            ),
        },
    )
