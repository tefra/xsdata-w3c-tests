from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Doc:
    """
    :ivar target:
    :ivar equiv:
    """
    class Meta:
        name = "doc"

    target: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )
    equiv: List[str] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
