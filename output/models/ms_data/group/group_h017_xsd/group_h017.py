from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class A:
    """
    :ivar x1:
    :ivar x2:
    :ivar y1:
    :ivar y2:
    """
    x1: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=2,
            max_occurs=4,
            sequential=True
        )
    )
    x2: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=2,
            max_occurs=4,
            sequential=True
        )
    )
    y1: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=4
        )
    )
    y2: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=4
        )
    )


@dataclass
class Elem:
    """
    :ivar x1:
    :ivar x2:
    :ivar y1:
    :ivar y2:
    """
    class Meta:
        name = "elem"

    x1: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=2,
            max_occurs=2,
            sequential=True
        )
    )
    x2: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=2,
            max_occurs=2,
            sequential=True
        )
    )
    y1: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=2
        )
    )
    y2: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=2
        )
    )


@dataclass
class Doc:
    """
    :ivar elem:
    """
    class Meta:
        name = "doc"

    elem: Optional[Elem] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )