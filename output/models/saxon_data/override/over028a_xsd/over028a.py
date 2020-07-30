from dataclasses import dataclass, field
from typing import Optional


@dataclass
class NewSize:
    """
    :ivar value:
    """
    class Meta:
        name = "newSize"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True,
            max_inclusive=16
        )
    )
