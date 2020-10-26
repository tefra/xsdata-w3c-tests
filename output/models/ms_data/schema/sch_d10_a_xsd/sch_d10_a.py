from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "ns-a"


@dataclass
class ACt:
    """
    :ivar c21_or_c22:
    """
    class Meta:
        name = "a-ct"

    c21_or_c22: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "c21",
                    "type": int,
                    "namespace": "",
                },
                {
                    "name": "c22",
                    "type": int,
                    "namespace": "",
                },
            ),
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
