from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "ns-a"


@dataclass
class ACt:
    """
    :ivar c21:
    :ivar c22:
    """
    class Meta:
        name = "a-ct"

    c21: List[int] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 3,
        }
    )
    c22: List[int] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 3,
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
class E1(ACt):
    class Meta:
        name = "e1"
        namespace = "ns-a"
