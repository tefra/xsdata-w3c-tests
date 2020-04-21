from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "ns-a"


@dataclass
class BCt:
    """
    :ivar b1:
    :ivar b2:
    """
    class Meta:
        name = "b-ct"

    b1: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="ns-a"
        )
    )
    b2: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="ns-a"
        )
    )


@dataclass
class Root:
    """
    :ivar any_element:
    """
    class Meta:
        name = "root"
        namespace = "ns-a"

    any_element: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class E1(BCt):
    class Meta:
        name = "e1"
        namespace = "ns-a"
