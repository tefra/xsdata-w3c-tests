from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional


@dataclass
class Section:
    """
    :ivar head:
    :ivar section:
    :ivar nr:
    """
    class Meta:
        name = "section"

    head: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    section: List["Section"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    nr: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
