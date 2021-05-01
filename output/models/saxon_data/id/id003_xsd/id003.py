from dataclasses import dataclass, field
from typing import Dict, List, Optional, Type


@dataclass
class Node:
    class Meta:
        name = "node"

    node_or_id: List[object] = field(
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
                },
            ),
        }
    )
    id_one: Optional[str] = field(
        default=None,
        metadata={
            "name": "id-one",
            "type": "Attribute",
        }
    )
    any_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
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
