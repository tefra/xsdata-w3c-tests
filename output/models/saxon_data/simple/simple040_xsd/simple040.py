from dataclasses import dataclass, field
from typing import Optional


@dataclass
class E:
    class Meta:
        name = "e"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "pattern": r"[a-z-[m-n]]*",
        }
    )
