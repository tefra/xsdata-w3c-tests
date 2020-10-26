from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Doc:
    """
    :ivar a_or_b:
    """
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    a_or_b: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "a",
                    "type": object,
                },
                {
                    "name": "b",
                    "type": object,
                },
            ),
            "min_occurs": 2,
            "max_occurs": 4,
        }
    )
