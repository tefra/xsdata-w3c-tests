from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ns-b"


@dataclass
class FooC:
    class Meta:
        name = "foo_c"
        namespace = "ns-b"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )
