from dataclasses import dataclass, field
from typing import List


@dataclass
class Node:
    """
    :ivar node:
    :ivar id:
    :ivar idrefs:
    :ivar id_attribute:
    :ivar idrefs_attribute:
    """
    class Meta:
        name = "node"

    node: List["Node"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    id: List[List[str]] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "tokens": True,
        }
    )
    idrefs: List[List[str]] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "tokens": True,
        }
    )
    id_attribute: List[str] = field(
        default_factory=list,
        metadata={
            "name": "id",
            "type": "Attribute",
            "tokens": True,
        }
    )
    idrefs_attribute: List[str] = field(
        default_factory=list,
        metadata={
            "name": "idrefs",
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
