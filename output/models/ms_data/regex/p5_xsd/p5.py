from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Regex:
    att: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_exclusive": 10,
            "pattern": r"[0-9]*",
        },
    )


@dataclass
class Doc:
    class Meta:
        name = "doc"

    elem: list[Regex] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
