from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "psContents"


@dataclass
class A:
    class Meta:
        name = "a"
        namespace = "psContents"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "process_contents": "skip",
        }
    )
