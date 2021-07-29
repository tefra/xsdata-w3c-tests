from dataclasses import dataclass, field
from typing import List, Optional, Type


@dataclass
class PseudoId:
    class Meta:
        name = "pseudoID"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    a: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class PseudoIdref:
    class Meta:
        name = "pseudoIDREF"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    a: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


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
                    "type": PseudoId,
                },
                {
                    "name": "idref",
                    "type": PseudoIdref,
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
