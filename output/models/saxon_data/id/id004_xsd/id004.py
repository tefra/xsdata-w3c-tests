from dataclasses import dataclass, field
from typing import Dict, List


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
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    id: List[List[str]] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807,
            tokens=True
        )
    )
    id_one: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="id-one",
            type="Attribute",
            tokens=True
        )
    )
    any_attributes: Dict = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="##any"
        )
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
        metadata=dict(
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
