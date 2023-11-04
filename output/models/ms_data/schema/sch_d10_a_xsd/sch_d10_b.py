from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "ns-a"


@dataclass
class BCt:
    class Meta:
        name = "b-ct"

    c21_or_c22: List[int] = field(
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
class BE1(BCt):
    class Meta:
        name = "b-e1"
        namespace = "ns-a"
