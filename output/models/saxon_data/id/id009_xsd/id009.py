from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef


@dataclass(kw_only=True)
class Node:
    class Meta:
        name = "node"

    node_or_id_or_idref: list[Node | Node.Id | Node.Idref] = field(
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

    @dataclass(kw_only=True)
    class Id:
        class Meta:
            global_type = False
            nillable = True

        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )

    @dataclass(kw_only=True)
    class Idref:
        class Meta:
            global_type = False
            nillable = True

        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )


@dataclass(kw_only=True)
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
