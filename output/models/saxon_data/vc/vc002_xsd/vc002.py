from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Temp:
    """
    :ivar value:
    """
    class Meta:
        name = "temp"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            pattern=r"2008.*"
        )
    )
