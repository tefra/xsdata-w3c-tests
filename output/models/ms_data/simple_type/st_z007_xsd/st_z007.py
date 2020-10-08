from dataclasses import dataclass, field
from typing import List


@dataclass
class Root:
    """
    :ivar e1:
    :ivar e2:
    """
    class Meta:
        name = "root"

    e1: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=10
        )
    )
    e2: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=10
        )
    )
