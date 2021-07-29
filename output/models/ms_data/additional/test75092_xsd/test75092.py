from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Foo:
    class Meta:
        name = "foo"

    a: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    any_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )
