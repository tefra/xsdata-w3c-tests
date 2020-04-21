from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Doc:
    """
    :ivar value:
    """
    class Meta:
        name = "doc"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            min_inclusive="-P3D",
            max_inclusive="P3D"
        )
    )
