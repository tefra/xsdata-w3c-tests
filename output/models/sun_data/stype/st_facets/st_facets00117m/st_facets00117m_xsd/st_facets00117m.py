from decimal import Decimal
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ST_facets"


@dataclass
class Test:
    """
    :ivar value:
    """
    class Meta:
        name = "test"
        namespace = "ST_facets"

    value: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            required=True,
            max_inclusive=100.0
        )
    )