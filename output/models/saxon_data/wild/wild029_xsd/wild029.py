from dataclasses import dataclass, field
from typing import List


@dataclass
class Eden:
    class Meta:
        name = "eden"

    a_or_any_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "a",
                    "type": str,
                    "namespace": "",
                },
                {
                    "wildcard": True,
                    "type": object,
                    "namespace": "##any",
                    "required": True,
                },
            ),
            "min_occurs": 1,
            "max_occurs": 3,
        }
    )
