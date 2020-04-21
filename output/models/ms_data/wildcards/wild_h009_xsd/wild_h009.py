from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Foo:
    """
    :ivar www_w3_org_1999_xhtml_element:
    """
    class Meta:
        name = "foo"

    www_w3_org_1999_xhtml_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="http://www.w3.org/1999/xhtml",
            required=True
        )
    )
