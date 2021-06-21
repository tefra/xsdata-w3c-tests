from dataclasses import dataclass, field
from typing import List, Type, Union


@dataclass
class Node:
    class Meta:
        name = "node"

    node_or_id_or_idrefs: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "node",
                    "type": Type["Node"],
                },
                {
                    "name": "id",
                    "type": List[Union[str, int]],
                    "default_factory": list,
                    "tokens": True,
                },
                {
                    "name": "idrefs",
                    "type": List[Union[str, int]],
                    "default_factory": list,
                    "tokens": True,
                },
            ),
        }
    )
    id_attribute: List[Union[str, int]] = field(
        default_factory=list,
        metadata={
            "name": "id",
            "type": "Attribute",
            "tokens": True,
        }
    )
    idrefs_attribute: List[Union[str, int]] = field(
        default_factory=list,
        metadata={
            "name": "idrefs",
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
