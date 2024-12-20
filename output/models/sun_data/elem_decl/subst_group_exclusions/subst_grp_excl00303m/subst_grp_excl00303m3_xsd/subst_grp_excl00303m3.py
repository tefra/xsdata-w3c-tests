from dataclasses import dataclass, field
from typing import Optional

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

    head: list[Head] = field(
        default_factory=list,
        metadata={
            "name": "Head",
            "type": "Element",
            "min_occurs": 1,
        },
    )
