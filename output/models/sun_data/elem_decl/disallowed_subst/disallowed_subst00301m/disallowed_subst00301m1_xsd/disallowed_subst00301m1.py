from dataclasses import dataclass, field
from typing import Optional, Union

__NAMESPACE__ = "ElemDecl/disallowedSubst"


@dataclass
class Head:
    class Meta:
        namespace = "ElemDecl/disallowedSubst"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class Member1:
    class Meta:
        namespace = "ElemDecl/disallowedSubst"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/disallowedSubst"

    member1_or_head: list[Union[Member1, Head]] = field(
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
