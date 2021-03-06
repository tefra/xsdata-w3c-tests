from dataclasses import dataclass, field
from typing import List, Type


@dataclass
class Node:
    class Meta:
        name = "node"

    node_or_mixed_a_or_mixed_b: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "node",
                    "type": Type["Node"],
                },
                {
                    "name": "mixedA",
                    "type": List[str],
                    "default_factory": list,
                    "tokens": True,
                },
                {
                    "name": "mixedB",
                    "type": List[str],
                    "default_factory": list,
                    "tokens": True,
                },
            ),
        }
    )
    mixed_a: List[str] = field(
        default_factory=list,
        metadata={
            "name": "mixedA",
            "type": "Attribute",
            "tokens": True,
        }
    )
    mixed_b: List[str] = field(
        default_factory=list,
        metadata={
            "name": "mixedB",
            "type": "Attribute",
            "tokens": True,
        }
    )


@dataclass
class Doc:
    class Meta:
        name = "doc"

    node: List[Node] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
