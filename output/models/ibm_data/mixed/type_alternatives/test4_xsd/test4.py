from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Example:
    """
    :ivar x:
    :ivar kind:
    """
    x: List[int] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    kind: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
