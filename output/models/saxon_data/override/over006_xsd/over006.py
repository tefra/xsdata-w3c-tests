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
        metadata=dict(
            type="Element",
            required=True
        )
    )
    section: List["Section"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    nr: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            required=True
        )
    )
