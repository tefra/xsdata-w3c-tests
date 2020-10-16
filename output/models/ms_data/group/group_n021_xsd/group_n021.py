from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Elem:
    """
    :ivar a1:
    :ivar a2:
    """
    class Meta:
        name = "elem"

    a1: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    a2: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
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
