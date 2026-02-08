from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-decimal-minExclusive-4-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDecimalMinExclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-decimal-minExclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-decimal-minExclusive-4-NS"

    value: Decimal = field(
        metadata={
            "min_exclusive": Decimal("-294253147230818967"),
        }
    )
