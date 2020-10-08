from dataclasses import dataclass, field
from typing import List


@dataclass
class Outer:
    """
    :ivar inner:
    """
    class Meta:
        name = "outer"

    inner: List[int] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=4
        )
    )
