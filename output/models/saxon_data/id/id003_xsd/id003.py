from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class Node:
    """
    :ivar node:
    :ivar id:
    :ivar id_one:
    :ivar any_attributes:
    """
    class Meta:
        name = "node"

    node: List["Node"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    id: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    id_one: Optional[str] = field(
        default=None,
        metadata={
            "name": "id-one",
            "type": "Attribute",
        }
    )
    any_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
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
