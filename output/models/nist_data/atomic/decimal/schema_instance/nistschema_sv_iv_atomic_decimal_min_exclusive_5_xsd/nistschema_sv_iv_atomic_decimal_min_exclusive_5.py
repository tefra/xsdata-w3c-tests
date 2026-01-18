from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-decimal-minExclusive-5-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDecimalMinExclusive5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-decimal-minExclusive-5"
        namespace = "NISTSchema-SV-IV-atomic-decimal-minExclusive-5-NS"

    value: Decimal = field(
        metadata={
            "required": True,
            "min_exclusive": Decimal("999999999999999998"),
        }
    )
