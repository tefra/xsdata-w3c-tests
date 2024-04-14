from dataclasses import dataclass, field
from typing import ForwardRef, List, Union


@dataclass
class Node:
    class Meta:
        name = "node"

    node_or_id_or_idrefs: List[Union["Node", "Node.Id", "Node.Idrefs"]] = (
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
    id_attribute: List[str] = field(
        default_factory=list,
        metadata={
            "name": "id",
            "type": "Attribute",
            "tokens": True,
        },
    )
    idrefs_attribute: List[str] = field(
        default_factory=list,
        metadata={
            "name": "idrefs",
            "type": "Attribute",
            "tokens": True,
        },
    )

    @dataclass
    class Id:
        value: List[str] = field(
            default_factory=list,
            metadata={
                "tokens": True,
            },
        )

    @dataclass
    class Idrefs:
        value: List[str] = field(
            default_factory=list,
            metadata={
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
