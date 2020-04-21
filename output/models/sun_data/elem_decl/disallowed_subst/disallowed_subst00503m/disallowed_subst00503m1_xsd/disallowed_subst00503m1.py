from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "ElemDecl/disallowedSubst"


@dataclass
class Type:
    pass


@dataclass
class Head(Type):
    class Meta:
        namespace = "ElemDecl/disallowedSubst"



@dataclass
class DerivedFromType(Type):
    class Meta:
        name = "derivedFromType"



@dataclass
class Member1(DerivedFromType):
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
        metadata=dict(
            name="Member1",
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    head: List[Head] = field(
        default_factory=list,
        metadata=dict(
            name="Head",
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
