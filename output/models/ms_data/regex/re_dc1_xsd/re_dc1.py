from dataclasses import dataclass, field
from typing import List


@dataclass
class Doc:
    class Meta:
        name = "doc"

    elem: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "pattern": r"AF01D1",
            "format": "base16",
        }
    )
