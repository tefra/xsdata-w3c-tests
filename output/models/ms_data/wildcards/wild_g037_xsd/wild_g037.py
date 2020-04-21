from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://foobar"


@dataclass
class Foo:
    """
    :ivar www_w3_org_1999_xhtml_element:
    """
    class Meta:
        name = "foo"
        namespace = "http://foobar"

    www_w3_org_1999_xhtml_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##local http://www.w3.org/1999/xhtml",
            required=True
        )
    )
