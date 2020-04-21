from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class B:
    """
    :ivar a:
    :ivar b:
    :ivar c:
    :ivar one_com_element:
    """
    class Meta:
        name = "b"

    a: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=5
        )
    )
    b: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=5
        )
    )
    c: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    one_com_element: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="http://one.com/",
            min_occurs=2,
            max_occurs=2
        )
    )


@dataclass
class E(B):
    """
    :ivar e:
    :ivar f:
    :ivar two_com_element:
    """
    class Meta:
        name = "e"

    e: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element"
        )
    )
    f: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=4
        )
    )
    two_com_element: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="http://two.com/",
            min_occurs=2,
            max_occurs=2
        )
    )


@dataclass
class Doc(E):
    class Meta:
        name = "doc"
