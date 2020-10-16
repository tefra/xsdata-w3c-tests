from dataclasses import dataclass, field
from typing import List


@dataclass
class Doc:
    """
    :ivar elem:
    """
    class Meta:
        name = "doc"

    elem: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "pattern": r"[a-c-1-4x-z-7-9]*",
        }
    )
