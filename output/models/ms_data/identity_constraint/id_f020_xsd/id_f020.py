from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class T:
    """
    :ivar row:
    :ivar col:
    """
    class Meta:
        name = "t"

    row: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    col: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
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
