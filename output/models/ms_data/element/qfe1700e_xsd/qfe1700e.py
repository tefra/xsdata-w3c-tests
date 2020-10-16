from dataclasses import dataclass, field
from typing import Optional


@dataclass
class E1:
    """
    :ivar value:
    """
    class Meta:
        name = "e1"
        nillable = True

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Root:
    """
    :ivar e1:
    """
    class Meta:
        name = "root"

    e1: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "nillable": True,
        }
    )
