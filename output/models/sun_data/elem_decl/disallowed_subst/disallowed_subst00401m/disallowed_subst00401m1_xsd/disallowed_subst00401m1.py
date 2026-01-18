from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "ElemDecl/disallowedSubst"


@dataclass(kw_only=True)
class Head:
    class Meta:
        namespace = "ElemDecl/disallowedSubst"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class Member1:
    class Meta:
        namespace = "ElemDecl/disallowedSubst"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class Member2:
    class Meta:
        namespace = "ElemDecl/disallowedSubst"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/disallowedSubst"

    member2_or_member1_or_head: list[Member2 | Member1 | Head] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "Member2",
                    "type": Member2,
                },
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
