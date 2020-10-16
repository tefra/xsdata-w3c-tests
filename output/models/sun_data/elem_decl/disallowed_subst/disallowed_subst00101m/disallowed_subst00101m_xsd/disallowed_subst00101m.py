from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "ElemDecl/disallowedSubst"


@dataclass
class HeadType:
    """
    :ivar ear:
    :ivar eye:
    """
    ear: Optional[object] = field(
        default=None,
        metadata={
            "name": "Ear",
            "type": "Element",
            "namespace": "ElemDecl/disallowedSubst",
            "required": True,
        }
    )
    eye: Optional[object] = field(
        default=None,
        metadata={
            "name": "Eye",
            "type": "Element",
            "namespace": "ElemDecl/disallowedSubst",
            "required": True,
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
    """
    :ivar member1:
    :ivar head:
    """
    class Meta:
        name = "root"
        namespace = "ElemDecl/disallowedSubst"

    member1: List[Member1] = field(
        default_factory=list,
        metadata={
            "name": "Member1",
            "type": "Element",
            "min_occurs": 1,
        }
    )
    head: List[Head] = field(
        default_factory=list,
        metadata={
            "name": "Head",
            "type": "Element",
            "min_occurs": 1,
        }
    )
