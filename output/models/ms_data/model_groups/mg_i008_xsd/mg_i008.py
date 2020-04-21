from dataclasses import dataclass, field
from typing import List


@dataclass
class Foo:
    """
    :ivar www_w3_org_1999_xhtml_element:
    """
    class Meta:
        name = "foo"

    www_w3_org_1999_xhtml_element: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class Doc(Foo):
    class Meta:
        name = "doc"
