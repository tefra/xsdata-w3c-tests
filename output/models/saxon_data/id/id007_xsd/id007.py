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
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    mixed_a: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="mixedA",
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    mixed_b: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="mixedB",
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    mixed_a_attribute: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="mixedA",
            type="Attribute",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    mixed_b_attribute: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="mixedB",
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
