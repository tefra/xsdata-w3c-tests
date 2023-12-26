from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = "ST_facets"


@dataclass
class Test:
    class Meta:
        name = "test"
        namespace = "ST_facets"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
            "max_exclusive": Decimal("11"),
        },
    )
