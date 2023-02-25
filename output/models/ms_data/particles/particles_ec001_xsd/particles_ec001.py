from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Doc:
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    a1_or_a2: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "a1",
                    "type": object,
                },
                {
                    "name": "a2",
                    "type": object,
                },
            ),
            "max_occurs": 2,
        }
    )
