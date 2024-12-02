from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Bad:
    class Meta:
        name = "bad"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )


@dataclass
class Good:
    class Meta:
        name = "good"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
