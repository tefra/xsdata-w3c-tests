from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "ElemDecl/abstract"


@dataclass
class HeadType:
    ear: Optional[object] = field(
        default=None,
        metadata={
            "name": "Ear",
            "type": "Element",
            "namespace": "ElemDecl/abstract",
        }
    )
    eye: Optional[object] = field(
        default=None,
        metadata={
            "name": "Eye",
            "type": "Element",
            "namespace": "ElemDecl/abstract",
        }
    )


@dataclass
class Member1(HeadType):
    class Meta:
        namespace = "ElemDecl/abstract"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/abstract"

    member1: List[Member1] = field(
        default_factory=list,
        metadata={
            "name": "Member1",
            "type": "Element",
        }
    )
