from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "ElemDecl/substGroupExclusions"


@dataclass
class HeadType:
    """
    :ivar ear:
    :ivar eye:
    """
    ear: Optional[object] = field(
        default=None,
        metadata=dict(
            name="Ear",
            type="Element",
            namespace="ElemDecl/substGroupExclusions",
            required=True
        )
    )
    eye: Optional[object] = field(
        default=None,
        metadata=dict(
            name="Eye",
            type="Element",
            namespace="ElemDecl/substGroupExclusions",
            required=True
        )
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
    """
    :ivar member1:
    :ivar head:
    """
    class Meta:
        name = "root"
        namespace = "ElemDecl/substGroupExclusions"

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