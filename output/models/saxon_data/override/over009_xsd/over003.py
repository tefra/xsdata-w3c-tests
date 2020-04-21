from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Para2:
    """
    :ivar value:
    """
    class Meta:
        name = "para2"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            pattern=r"[0-9]+-[0-9]+-[0-9]+"
        )
    )
