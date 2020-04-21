from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Foo:
    """
    :ivar a:
    :ivar www_w3_org_1999_xhtml_element:
    :ivar d:
    :ivar c:
    :ivar b:
    :ivar b2:
    """
    class Meta:
        name = "foo"

    a: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    www_w3_org_1999_xhtml_element: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    d: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    c: Optional[bool] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
    )
    b: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
    )
    b2: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
    )


@dataclass
class Doc(Foo):
    class Meta:
        name = "doc"
