from dataclasses import dataclass, field
from typing import ForwardRef, Union


@dataclass
class Node:
    class Meta:
        name = "node"

    node_or_id: list[Union["Node", str]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "node",
                    "type": ForwardRef("Node"),
                },
                {
                    "name": "id",
                    "type": str,
                },
            ),
        },
    )


@dataclass
class Doc:
    class Meta:
        name = "doc"

    node: list[Node] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
