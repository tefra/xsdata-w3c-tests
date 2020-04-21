from dataclasses import dataclass, field
from typing import List


@dataclass
class Eden:
    """
    :ivar any_element:
    """
    class Meta:
        name = "eden"

    any_element: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
