from dataclasses import dataclass, field
from lxml.etree import QName
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
    id: List[str] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    id_one: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="id-one",
            type="Attribute",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    any_attributes: Dict[QName, str] = field(
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