from dataclasses import dataclass, field
from typing import Optional, Union

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
class Member3(HeadType):
    class Meta:
        namespace = "ElemDecl/substGroupExclusions"

    nose: Optional[object] = field(
        default=None,
        metadata={
            "name": "Nose",
            "type": "Element",
        },
    )


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/substGroupExclusions"

    member3_or_member1_or_head: list[Union[Member3, Member1, Head]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "Member3",
                    "type": Member3,
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
