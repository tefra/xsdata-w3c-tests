from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Para:
    """
    :ivar value:
    """
    class Meta:
        name = "para"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "pattern": r"[0-9]+-[0-9]+-[0-9]+",
        }
    )


@dataclass
class Para2:
    """
    :ivar value:
    """
    class Meta:
        name = "para2"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "pattern": r"[0-9]+-[0-9]+-[0-9]+",
        }
    )
