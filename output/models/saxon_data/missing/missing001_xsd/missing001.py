from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Bad:
    class Meta:
        name = "bad"


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
