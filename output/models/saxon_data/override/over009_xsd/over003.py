from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Para:
    class Meta:
        name = "para"

    value: Optional[str] = field(
        default=None,
        metadata={
            "pattern": r"[0-9]+-[0-9]+-[0-9]+",
        }
    )


@dataclass
class Para2:
    class Meta:
        name = "para2"

    value: Optional[str] = field(
        default=None,
        metadata={
            "pattern": r"[0-9]+-[0-9]+-[0-9]+",
        }
    )
