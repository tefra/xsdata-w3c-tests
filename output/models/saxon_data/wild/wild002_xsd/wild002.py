from dataclasses import dataclass, field
from typing import List


@dataclass
class Eden:
    class Meta:
        name = "eden"

    any_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "process_contents": "skip",
        }
    )
