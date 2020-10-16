from dataclasses import dataclass, field
from typing import List


@dataclass
class Base:
    """
    :ivar e1:
    :ivar e2:
    """
    class Meta:
        name = "base"

    e1: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 5,
        }
    )
    e2: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 5,
        }
    )
