from dataclasses import dataclass, field
from typing import List, Optional, Type


@dataclass
class PseudoId:
    """
    :ivar value:
    :ivar a:
    """
    class Meta:
        name = "pseudoID"

    value: Optional[str] = field(
        default=None,
    )
    a: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class PseudoIdref:
    """
    :ivar value:
    :ivar a:
    """
    class Meta:
        name = "pseudoIDREF"

    value: Optional[str] = field(
        default=None,
    )
    a: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Node:
    """
    :ivar node_or_id_or_idref:
    """
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
