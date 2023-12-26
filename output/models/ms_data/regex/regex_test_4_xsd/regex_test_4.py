from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Doc:
    class Meta:
        name = "doc"

    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"(\P{Lu}+\p{Lu})\s(\P{Lu}+\p{Lu})",
        },
    )
