from dataclasses import dataclass, field
from typing import List, Optional, Union

__NAMESPACE__ = "ElemDecl/disallowedSubst"


@dataclass
class HeadType:
    ear: Optional[object] = field(
        default=None,
        metadata={
            "name": "Ear",
            "type": "Element",
            "namespace": "ElemDecl/disallowedSubst",
        }
    )
    eye: Optional[object] = field(
        default=None,
        metadata={
            "name": "Eye",
            "type": "Element",
            "namespace": "ElemDecl/disallowedSubst",
        }
    )


@dataclass
class Head(HeadType):
    class Meta:
        namespace = "ElemDecl/disallowedSubst"


@dataclass
class Member1(HeadType):
    class Meta:
        namespace = "ElemDecl/disallowedSubst"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/disallowedSubst"

    member1_or_head: List[Union[Head, Member1]] = field(
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
        }
    )
