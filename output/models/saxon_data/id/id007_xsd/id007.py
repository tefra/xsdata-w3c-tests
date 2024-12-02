from dataclasses import dataclass, field
from typing import ForwardRef, Union


@dataclass
class Node:
    class Meta:
        name = "node"

    node_or_mixed_a_or_mixed_b: list[
        Union["Node", "Node.MixedA", "Node.MixedB"]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "node",
                    "type": ForwardRef("Node"),
                },
                {
                    "name": "mixedA",
                    "type": ForwardRef("Node.MixedA"),
                },
                {
                    "name": "mixedB",
                    "type": ForwardRef("Node.MixedB"),
                },
            ),
        },
    )
    mixed_a_attribute: list[str] = field(
        default_factory=list,
        metadata={
            "name": "mixedA",
            "type": "Attribute",
            "tokens": True,
        },
    )
    mixed_b_attribute: list[str] = field(
        default_factory=list,
        metadata={
            "name": "mixedB",
            "type": "Attribute",
            "tokens": True,
        },
    )

    @dataclass
    class MixedA:
        value: list[str] = field(
            default_factory=list,
            metadata={
                "tokens": True,
            },
        )

    @dataclass
    class MixedB:
        value: list[str] = field(
            default_factory=list,
            metadata={
                "tokens": True,
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
