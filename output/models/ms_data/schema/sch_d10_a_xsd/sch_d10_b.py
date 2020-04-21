from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "ns-a"


@dataclass
class BCt:
    """
    :ivar c21:
    :ivar c22:
    """
    class Meta:
        name = "b-ct"

    c21: List[int] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=3
        )
    )
    c22: List[int] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=3
        )
    )


@dataclass
class BE1(BCt):
    class Meta:
        name = "b-e1"
        namespace = "ns-a"
