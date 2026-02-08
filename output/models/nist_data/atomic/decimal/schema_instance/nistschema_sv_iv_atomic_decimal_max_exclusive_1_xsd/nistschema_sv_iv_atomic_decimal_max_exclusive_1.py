from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-decimal-maxExclusive-1-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDecimalMaxExclusive1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-decimal-maxExclusive-1"
        namespace = "NISTSchema-SV-IV-atomic-decimal-maxExclusive-1-NS"

    value: Decimal = field(
        metadata={
            "max_exclusive": Decimal("-999999999999999998"),
        }
    )
