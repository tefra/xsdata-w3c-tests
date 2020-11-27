from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Doc:
    class Meta:
        name = "doc"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": "2000-01-01T00:00:00Z",
            "max_inclusive": "2999-12-31T23:59:59Z",
        }
    )
