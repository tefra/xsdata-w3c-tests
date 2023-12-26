from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Doc:
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    x_or_y: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "x",
                    "type": object,
                },
                {
                    "name": "y",
                    "type": object,
                },
            ),
            "max_occurs": 2,
        },
    )
