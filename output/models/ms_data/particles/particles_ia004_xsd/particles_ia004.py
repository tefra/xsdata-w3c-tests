from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Base:
    """
    :ivar e1:
    :ivar e2:
    """
    class Meta:
        name = "base"

    e1: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://xsdtesting",
            min_occurs=2,
            max_occurs=6
        )
    )
    e2: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://xsdtesting",
            min_occurs=2,
            max_occurs=6
        )
    )


@dataclass
class Doc:
    """
    :ivar e1:
    :ivar e2:
    """
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    e1: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=2,
            max_occurs=2
        )
    )
    e2: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=3,
            max_occurs=5
        )
    )
