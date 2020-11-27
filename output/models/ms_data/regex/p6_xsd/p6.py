from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Regex:
    att: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_exclusive": 10,
            "pattern": r"\-[0-9]*",
        }
    )


@dataclass
class Doc:
    class Meta:
        name = "doc"

    elem: List[Regex] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
