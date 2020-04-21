from dataclasses import dataclass, field
from typing import List, Union


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
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    id: List[Union[str, int]] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    idrefs: List[Union[str, int]] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    id_attribute: List[Union[str, int]] = field(
        default_factory=list,
        metadata=dict(
            name="id",
            type="Attribute",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    idrefs_attribute: List[Union[str, int]] = field(
        default_factory=list,
        metadata=dict(
            name="idrefs",
            type="Attribute",
            min_occurs=0,
            max_occurs=9223372036854775807
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
