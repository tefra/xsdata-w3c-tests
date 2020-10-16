from dataclasses import dataclass, field
from typing import List


@dataclass
class Node:
    """
    :ivar node:
    :ivar mixed_a:
    :ivar mixed_b:
    :ivar mixed_a_attribute:
    :ivar mixed_b_attribute:
    """
    class Meta:
        name = "node"

    node: List["Node"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    mixed_a: List[List[str]] = field(
        default_factory=list,
        metadata={
            "name": "mixedA",
            "type": "Element",
            "tokens": True,
        }
    )
    mixed_b: List[List[str]] = field(
        default_factory=list,
        metadata={
            "name": "mixedB",
            "type": "Element",
            "tokens": True,
        }
    )
    mixed_a_attribute: List[str] = field(
        default_factory=list,
        metadata={
            "name": "mixedA",
            "type": "Attribute",
            "tokens": True,
        }
    )
    mixed_b_attribute: List[str] = field(
        default_factory=list,
        metadata={
            "name": "mixedB",
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
