from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "urn:test"


@dataclass
class Root:
    class Meta:
        namespace = "urn:test"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "A",
                    "type": str,
                },
                {
                    "name": "B1",
                    "type": str,
                },
                {
                    "name": "B2",
                    "type": str,
                },
                {
                    "name": "B3",
                    "type": str,
                },
                {
                    "name": "B4",
                    "type": str,
                },
                {
                    "name": "B5",
                    "type": str,
                },
            ),
        },
    )
