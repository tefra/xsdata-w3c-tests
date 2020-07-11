from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Foo:
    """
    :ivar b:
    :ivar b2:
    :ivar w3_org_1999_xhtml_element:
    :ivar c:
    :ivar a:
    :ivar d:
    """
    class Meta:
        name = "foo"

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
    w3_org_1999_xhtml_element: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    c: Optional[bool] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
    )
    a: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
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


@dataclass
class Doc(Foo):
    class Meta:
        name = "doc"
