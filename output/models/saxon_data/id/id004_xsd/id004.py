from dataclasses import dataclass, field
from typing import Dict, ForwardRef, List, Union


@dataclass
class Node:
    class Meta:
        name = "node"

    node_or_id: List[Union["Node", List[str]]] = field(
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
                    "type": List[str],
                    "default_factory": list,
                    "tokens": True,
                },
            ),
        },
    )
    id_one: List[str] = field(
        default_factory=list,
        metadata={
            "name": "id-one",
            "type": "Attribute",
            "tokens": True,
        },
    )
    any_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
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
