from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Message:
    """
    :ivar value:
    """
    class Meta:
        name = "message"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            max_length=25.0
        )
    )
