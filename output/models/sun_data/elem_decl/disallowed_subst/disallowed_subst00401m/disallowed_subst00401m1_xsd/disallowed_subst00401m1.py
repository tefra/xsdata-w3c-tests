from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "ElemDecl/disallowedSubst"


@dataclass
class Head:
    """
    :ivar any_element:
    """
    class Meta:
        namespace = "ElemDecl/disallowedSubst"

    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )


@dataclass
class Member1:
    """
    :ivar any_element:
    """
    class Meta:
        namespace = "ElemDecl/disallowedSubst"

    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )


@dataclass
class Member2:
    """
    :ivar any_element:
    """
    class Meta:
        namespace = "ElemDecl/disallowedSubst"

    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )


@dataclass
class Root:
    """
    :ivar member2:
    :ivar member1:
    :ivar head:
    """
    class Meta:
        name = "root"
        namespace = "ElemDecl/disallowedSubst"

    member2: List[Member2] = field(
        default_factory=list,
        metadata=dict(
            name="Member2",
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
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
