from dataclasses import dataclass, field
from typing import List


@dataclass
class Doc:
    """
    :ivar any_element:
    """
    class Meta:
        name = "doc"

    any_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "min_occurs": 1,
        }
    )
