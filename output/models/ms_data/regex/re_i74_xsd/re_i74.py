from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Regex:
    att: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"(\t|\s)a(\r\n|\r|\n|\s)+(\s|\t)b(\s|\r\n|\r|\n)*",
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
