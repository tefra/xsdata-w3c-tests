from dataclasses import dataclass, field
from typing import List


@dataclass
class Node:
    """
    :ivar node:
    :ivar id:
    :ivar idref:
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
            "nillable": True,
        }
    )
    idref: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "nillable": True,
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
