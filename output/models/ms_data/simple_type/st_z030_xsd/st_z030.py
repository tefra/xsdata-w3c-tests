from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Ct:
    """
    :ivar e1:
    :ivar e2:
    """
    class Meta:
        name = "ct"

    e1: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_exclusive": 2,
            "min_inclusive": 2,
        }
    )
    e2: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_exclusive": 2,
            "min_inclusive": 3,
        }
    )


@dataclass
class Root(Ct):
    pass
