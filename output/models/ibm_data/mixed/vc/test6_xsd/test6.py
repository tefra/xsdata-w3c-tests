from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Example:
    """
    :ivar value:
    """
    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
