from dataclasses import dataclass, field
from typing import ForwardRef, Optional, Union


@dataclass
class PseudoId:
    class Meta:
        name = "pseudoID"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    a: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class PseudoIdref:
    class Meta:
        name = "pseudoIDREF"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    a: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Node:
    class Meta:
        name = "node"

    node_or_id_or_idref: list[Union["Node", PseudoId, PseudoIdref]] = field(
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
                    "type": PseudoId,
                },
                {
                    "name": "idref",
                    "type": PseudoIdref,
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
