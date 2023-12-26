from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "ns-a"


@dataclass
class BCt:
    class Meta:
        name = "b-ct"

    b1_or_b2: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "b1",
                    "type": object,
                    "namespace": "ns-a",
                },
                {
                    "name": "b2",
                    "type": object,
                    "namespace": "ns-a",
                },
            ),
        },
    )
    b3_or_b4: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "b3",
                    "type": object,
                    "namespace": "ns-a",
                },
                {
                    "name": "b4",
                    "type": object,
                    "namespace": "ns-a",
                },
            ),
        },
    )


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "ns-a"

    any_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class E1(BCt):
    class Meta:
        name = "e1"
        namespace = "ns-a"
