from dataclasses import dataclass, field
from typing import ForwardRef, List, Optional, Union


@dataclass
class Node:
    class Meta:
        name = "node"

    node_or_id_or_idref: List[Union["Node", "Node.Id", "Node.Idref"]] = field(
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
                    "name": "idref",
                    "type": ForwardRef("Node.Idref"),
                },
            ),
        },
    )

    @dataclass
    class Id:
        class Meta:
            global_type = False
            nillable = True

        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass
    class Idref:
        class Meta:
            global_type = False
            nillable = True

        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
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
