from dataclasses import dataclass, field
from typing import ForwardRef, Union


@dataclass
class Node:
    class Meta:
        name = "node"

    node_or_id_or_idrefs: list[Union["Node", "Node.Id", "Node.Idrefs"]] = (
        field(
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
                        "type": ForwardRef("Node.Id"),
                    },
                    {
                        "name": "idrefs",
                        "type": ForwardRef("Node.Idrefs"),
                    },
                ),
            },
        )
    )
    id_attribute: list[str] = field(
        default_factory=list,
        metadata={
            "name": "id",
            "type": "Attribute",
            "tokens": True,
        },
    )
    idrefs_attribute: list[str] = field(
        default_factory=list,
        metadata={
            "name": "idrefs",
            "type": "Attribute",
            "tokens": True,
        },
    )

    @dataclass
    class Id:
        value: list[str] = field(
            default_factory=list,
            metadata={
                "tokens": True,
            },
        )

    @dataclass
    class Idrefs:
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
