from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

__NAMESPACE__ = "ST_facets"


@dataclass(kw_only=True)
class Test:
    class Meta:
        name = "test"
        namespace = "ST_facets"

    value: Decimal = field(
        metadata={
            "max_exclusive": Decimal("11"),
        }
    )
