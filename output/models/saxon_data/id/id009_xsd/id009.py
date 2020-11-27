from dataclasses import dataclass, field
from typing import List, Type


@dataclass
class Node:
    class Meta:
        name = "node"

    node_or_id_or_idref: List[object] = field(
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
                    "type": str,
                    "nillable": True,
                },
                {
                    "name": "idref",
                    "type": str,
                    "nillable": True,
                },
            ),
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
