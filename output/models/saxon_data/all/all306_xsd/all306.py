from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class B:
    """
    :ivar content:
    :ivar a:
    :ivar b:
    :ivar c:
    """
    class Meta:
        name = "b"

    content: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any"
        )
    )
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


@dataclass
class Ext(B):
    """
    :ivar content:
    :ivar d:
    :ivar e:
    """
    class Meta:
        name = "ext"

    content: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any"
        )
    )
    d: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element"
        )
    )
    e: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=4
        )
    )


@dataclass
class Doc(Ext):
    class Meta:
        name = "doc"
