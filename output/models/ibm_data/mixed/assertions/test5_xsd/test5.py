from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Value:
    """
    :ivar value:
    """
    class Meta:
        name = "value"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
