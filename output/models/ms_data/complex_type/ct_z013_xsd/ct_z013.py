from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "ns"


@dataclass
class Ct:
    class Meta:
        name = "CT"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "a",
                    "type": int,
                    "namespace": "",
                },
            ),
        }
    )


@dataclass
class E(Ct):
    class Meta:
        name = "e"
        namespace = "ns"
