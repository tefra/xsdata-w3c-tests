from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class B:
    """
    :ivar a:
    :ivar b:
    :ivar c:
    :ivar d:
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
            min_occurs=1,
            max_occurs=5
        )
    )
    c: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=2,
            max_occurs=9223372036854775807
        )
    )
    d: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )


@dataclass
class E(B):
    """
    :ivar e:
    :ivar f:
    :ivar g:
    """
    class Meta:
        name = "e"

    e: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )
    f: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=3,
            max_occurs=4
        )
    )
    g: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=2,
            max_occurs=4
        )
    )


@dataclass
class Doc(E):
    class Meta:
        name = "doc"
