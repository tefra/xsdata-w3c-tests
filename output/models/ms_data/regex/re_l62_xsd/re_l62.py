from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Regex:
    att: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\p{IsHiragana}+",
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
            "min_occurs": 1,
        }
    )
