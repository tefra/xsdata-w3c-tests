from dataclasses import dataclass, field
from typing import List, Optional


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
    id: List[PseudoId] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    idref: List[PseudoIdref] = field(
        default_factory=list,
        metadata={
            "type": "Element",
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
