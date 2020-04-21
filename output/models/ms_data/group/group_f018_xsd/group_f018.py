from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class B:
    """
    :ivar x:
    """
    x: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )


@dataclass
class Elem(B):
    """
    :ivar a1:
    :ivar a2:
    """
    class Meta:
        name = "elem"

    a1: List[object] = field(
        default_factory=list,
        metadata=dict(
            name="A1",
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=2
        )
    )
    a2: List[object] = field(
        default_factory=list,
        metadata=dict(
            name="A2",
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
