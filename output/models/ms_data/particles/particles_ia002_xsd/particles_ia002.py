from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class T1:
    """
    :ivar a:
    :ivar b:
    """
    class Meta:
        name = "t1"

    a: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://xsdtesting",
            required=True
        )
    )
    b: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://xsdtesting",
            required=True
        )
    )


@dataclass
class Base:
    """
    :ivar e1:
    :ivar e2:
    """
    class Meta:
        name = "base"

    e1: List[T1] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://xsdtesting",
            min_occurs=2,
            max_occurs=6,
            nillable=True
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

    e1: List[T1] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=2,
            max_occurs=2,
            nillable=True
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
