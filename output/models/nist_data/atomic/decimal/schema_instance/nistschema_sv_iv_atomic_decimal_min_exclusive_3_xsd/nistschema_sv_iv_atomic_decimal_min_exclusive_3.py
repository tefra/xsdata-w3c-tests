from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-decimal-minExclusive-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDecimalMinExclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-decimal-minExclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-decimal-minExclusive-3-NS"

    value: Decimal = field(
        metadata={
            "min_exclusive": Decimal("-67428259604688900"),
        }
    )
