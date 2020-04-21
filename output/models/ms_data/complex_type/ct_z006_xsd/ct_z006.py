from dataclasses import dataclass, field
from typing import List


@dataclass
class Root:
    """
    :ivar element1:
    """
    class Meta:
        name = "root"

    element1: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=2,
            max_occurs=9223372036854775807
        )
    )
