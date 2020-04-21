from dataclasses import dataclass, field
from typing import List


@dataclass
class Root:
    """
    :ivar a:
    :ivar b:
    """
    a: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=2,
            max_occurs=2,
            sequential=True
        )
    )
    b: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=2,
            max_occurs=2,
            sequential=True
        )
    )
