from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Doc:
    class Meta:
        name = "doc"
        nillable = True

    value: Optional[str] = field(
        default="abc",
        metadata={
            "nillable": True,
        },
    )
