from dataclasses import dataclass, field
from typing import List


@dataclass
class T:
    """
    :ivar col:
    :ivar row:
    """
    class Meta:
        name = "t"

    col: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    row: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class Root:
    """
    :ivar t:
    """
    class Meta:
        name = "root"

    t: List[T] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
