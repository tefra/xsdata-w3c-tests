from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Root:
    class Meta:
        name = "root"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "length": 5,
        }
    )
