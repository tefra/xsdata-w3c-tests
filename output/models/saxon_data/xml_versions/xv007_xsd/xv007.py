from dataclasses import dataclass, field
from typing import List


@dataclass
class Doc:
    """
    :ivar item:
    """
    class Meta:
        name = "doc"

    item: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "pattern": r"\c",
        }
    )
