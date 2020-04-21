from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class B:
    """
    :ivar a:
    :ivar b:
    :ivar c:
    :ivar other_com_element:
    """
    a: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    b: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
    )
    c: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
    )
    other_com_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="http://open.com/ http://other.com/",
            required=True
        )
    )


@dataclass
class R:
    """
    :ivar a:
    :ivar b:
    :ivar c:
    :ivar open_com_element:
    :ivar other_com_element:
    """
    a: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    b: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
    )
    c: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
    )
    open_com_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="http://open.com/",
            required=True
        )
    )
    other_com_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="http://open.com/ http://other.com/",
            required=True
        )
    )


@dataclass
class Doc(R):
    class Meta:
        name = "doc"
