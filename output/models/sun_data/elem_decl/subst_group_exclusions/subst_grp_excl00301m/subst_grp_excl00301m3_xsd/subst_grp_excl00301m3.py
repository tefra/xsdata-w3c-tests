from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "ElemDecl/substGroupExclusions"


@dataclass
class HeadType:
    ear: Optional[object] = field(
        default=None,
        metadata={
            "name": "Ear",
            "type": "Element",
            "namespace": "ElemDecl/substGroupExclusions",
            "required": True,
        }
    )
    eye: Optional[object] = field(
        default=None,
        metadata={
            "name": "Eye",
            "type": "Element",
            "namespace": "ElemDecl/substGroupExclusions",
            "required": True,
        }
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

    head: List[Head] = field(
        default_factory=list,
        metadata={
            "name": "Head",
            "type": "Element",
            "min_occurs": 1,
        }
    )
