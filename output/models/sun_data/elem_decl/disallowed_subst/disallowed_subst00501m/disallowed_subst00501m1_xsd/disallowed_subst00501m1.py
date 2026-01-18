from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "ElemDecl/disallowedSubst"


@dataclass(kw_only=True)
class Head:
    class Meta:
        namespace = "ElemDecl/disallowedSubst"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class Member1:
    class Meta:
        namespace = "ElemDecl/disallowedSubst"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


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
