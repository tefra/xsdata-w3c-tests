from dataclasses import dataclass, field
from typing import Optional


@dataclass
class E:
    """
    :ivar value:
    """
    class Meta:
        name = "e"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            pattern=r"[a-z-+]*"
        )
    )
