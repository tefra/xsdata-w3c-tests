from dataclasses import dataclass, field
from decimal import Decimal
from typing import Dict, List, Optional


@dataclass
class Section:
    """
    :ivar head:
    :ivar section:
    :ivar id:
    :ivar other_attributes:
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
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            required=True
        )
    )
    other_attributes: Dict = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="##other"
        )
    )
    nr: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            required=True
        )
    )
