from dataclasses import dataclass, field
from typing import List


@dataclass
class Doc:
    """
    :ivar para:
    """
    class Meta:
        name = "doc"

    para: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "pattern": r"[0-9]+-[0-9]+-[0-9]+",
        }
    )
