from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "ElemDecl/disallowedSubst"


@dataclass
class Head:
    class Meta:
        namespace = "ElemDecl/disallowedSubst"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class Member1:
    class Meta:
        namespace = "ElemDecl/disallowedSubst"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/disallowedSubst"

    member1_or_head: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "Member1",
                    "type": str,
                },
                {
                    "name": "Head",
                    "type": str,
                },
            ),
        },
    )
