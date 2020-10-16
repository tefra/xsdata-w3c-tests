from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Elem:
    """
    :ivar b1:
    :ivar b2:
    """
    class Meta:
        name = "elem"

    b1: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 99999999999,
            "sequential": True,
        }
    )
    b2: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 99999999999,
            "sequential": True,
        }
    )


@dataclass
class Doc:
    """
    :ivar elem:
    """
    class Meta:
        name = "doc"

    elem: Optional[Elem] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
