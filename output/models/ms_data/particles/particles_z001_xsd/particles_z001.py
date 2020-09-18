from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Base:
    """
    :ivar annotation:
    :ivar element:
    :ivar any:
    """
    annotation: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
    )
    element: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807,
            sequential=True
        )
    )
    any: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807,
            sequential=True
        )
    )


@dataclass
class Derived:
    """
    :ivar annotation:
    :ivar element:
    :ivar any:
    """
    annotation: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
    )
    element: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    any: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class Doc:
    """
    :ivar elem:
    """
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    elem: Optional[Derived] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
    )
