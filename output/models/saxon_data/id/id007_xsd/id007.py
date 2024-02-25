from dataclasses import dataclass, field
from typing import List, Type, Union


@dataclass
class Node:
    class Meta:
        name = "node"

    node_or_mixed_a_or_mixed_b: List[
        Union["Node", "Node.MixedA", "Node.MixedB"]
    ] = field(
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
                    "type": Type["Node.MixedA"],
                },
                {
                    "name": "mixedB",
                    "type": Type["Node.MixedB"],
                },
            ),
        },
    )
    mixed_a_attribute: List[str] = field(
        default_factory=list,
        metadata={
            "name": "mixedA",
            "type": "Attribute",
            "tokens": True,
        },
    )
    mixed_b_attribute: List[str] = field(
        default_factory=list,
        metadata={
            "name": "mixedB",
            "type": "Attribute",
            "tokens": True,
        },
    )

    @dataclass
    class MixedA:
        value: List[str] = field(
            default_factory=list,
            metadata={
                "required": True,
                "tokens": True,
            },
        )

    @dataclass
    class MixedB:
        value: List[str] = field(
            default_factory=list,
            metadata={
                "required": True,
                "tokens": True,
            },
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
        },
    )
