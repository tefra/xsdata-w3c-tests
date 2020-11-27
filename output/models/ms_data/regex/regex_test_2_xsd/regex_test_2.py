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
            "pattern": r"(\p{Lu}\p{Ll}*)\s(\p{Lu}\p{Ll}*)",
        }
    )
