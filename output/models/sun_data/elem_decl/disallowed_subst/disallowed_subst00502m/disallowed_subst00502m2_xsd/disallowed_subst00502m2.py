from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "ElemDecl/disallowedSubst"


@dataclass
class TypeType:
    class Meta:
        name = "Type"


@dataclass
class Head(TypeType):
    class Meta:
        namespace = "ElemDecl/disallowedSubst"


@dataclass
class DerivedFromType(TypeType):
    class Meta:
        name = "derivedFromType"

    attr: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Member1(DerivedFromType):
    class Meta:
        namespace = "ElemDecl/disallowedSubst"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/disallowedSubst"

    member1: List[Member1] = field(
        default_factory=list,
        metadata={
            "name": "Member1",
            "type": "Element",
        }
    )
    head: List[Head] = field(
        default_factory=list,
        metadata={
            "name": "Head",
            "type": "Element",
        }
    )
