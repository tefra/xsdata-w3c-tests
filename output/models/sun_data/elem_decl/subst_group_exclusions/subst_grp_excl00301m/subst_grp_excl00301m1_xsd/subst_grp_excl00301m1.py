from dataclasses import dataclass, field
from typing import List, Optional, Union

__NAMESPACE__ = "ElemDecl/substGroupExclusions"


@dataclass
class HeadType:
    ear: Optional[object] = field(
        default=None,
        metadata={
            "name": "Ear",
            "type": "Element",
            "namespace": "ElemDecl/substGroupExclusions",
        },
    )
    eye: Optional[object] = field(
        default=None,
        metadata={
            "name": "Eye",
            "type": "Element",
            "namespace": "ElemDecl/substGroupExclusions",
        },
    )


@dataclass
class Head(HeadType):
    class Meta:
        namespace = "ElemDecl/substGroupExclusions"


@dataclass
class Member1(HeadType):
    class Meta:
        namespace = "ElemDecl/substGroupExclusions"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/substGroupExclusions"

    member1_or_head: List[Union[Member1, Head]] = field(
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
