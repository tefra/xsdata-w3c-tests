from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Root:
    """
    :ivar value:
    """
    class Meta:
        name = "root"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "pattern": r"[A-Z]{0,5}",
        }
    )
