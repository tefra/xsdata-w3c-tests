from dataclasses import dataclass, field
from typing import List, Type, Union


@dataclass
class Node:
    """
    :ivar node_or_id_or_idrefs:
    :ivar id:
    :ivar idrefs:
    """
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
                    "tokens": True,
                },
                {
                    "name": "idrefs",
                    "type": List[Union[str, int]],
                    "tokens": True,
                },
            ),
        }
    )
    id: List[Union[str, int]] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    idrefs: List[Union[str, int]] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )


@dataclass
class Doc:
    """
    :ivar node:
    """
    class Meta:
        name = "doc"

    node: List[Node] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
