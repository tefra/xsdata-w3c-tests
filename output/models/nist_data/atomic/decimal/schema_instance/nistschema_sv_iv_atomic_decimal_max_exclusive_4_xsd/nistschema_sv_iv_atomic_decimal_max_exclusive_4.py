from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-decimal-maxExclusive-4-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDecimalMaxExclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-decimal-maxExclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-decimal-maxExclusive-4-NS"

    value: Decimal = field(
        metadata={
            "max_exclusive": Decimal("-214771926190724381"),
        }
    )
