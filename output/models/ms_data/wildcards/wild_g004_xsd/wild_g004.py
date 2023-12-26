from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.w3.org/1999/xhtml"


@dataclass
class Foo:
    class Meta:
        name = "foo"
        namespace = "http://www.w3.org/1999/xhtml"

    other_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )
