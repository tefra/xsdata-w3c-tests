from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Bad:
    """
    :ivar value:
    """
    class Meta:
        name = "bad"

    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class Good:
    """
    :ivar value:
    """
    class Meta:
        name = "good"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
