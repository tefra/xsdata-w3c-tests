from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Elem:
    """
    :ivar b1:
    """
    class Meta:
        name = "elem"

    b1: Optional[object] = field(
        default=None,
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
