from decimal import Decimal
from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "a"


@dataclass
class Root:
    """
    :ivar content:
    :ivar element:
    :ivar version:
    """
    class Meta:
        name = "root"
        namespace = "a"

    content: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any"
        )
    )
    element: List[str] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    version: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
