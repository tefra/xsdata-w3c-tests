from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "ns-a"


@dataclass
class BCt:
    """
    :ivar b1:
    :ivar b2:
    :ivar b3:
    :ivar b4:
    """
    class Meta:
        name = "b-ct"

    b1: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "ns-a",
        }
    )
    b2: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "ns-a",
        }
    )
    b3: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "ns-a",
        }
    )
    b4: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "ns-a",
        }
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
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )


@dataclass
class E1(BCt):
    class Meta:
        name = "e1"
        namespace = "ns-a"
