from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "ElemDecl/disallowedSubst"


@dataclass(kw_only=True)
class Type:
    pass


@dataclass(kw_only=True)
class Head(Type):
    class Meta:
        namespace = "ElemDecl/disallowedSubst"


@dataclass(kw_only=True)
class DerivedFromType(Type):
    class Meta:
        name = "derivedFromType"

    attr: None | object = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Member1(DerivedFromType):
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
