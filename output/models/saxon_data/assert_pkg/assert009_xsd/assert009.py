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
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
