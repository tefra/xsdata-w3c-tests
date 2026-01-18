from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-decimal-maxExclusive-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDecimalMaxExclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-decimal-maxExclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-decimal-maxExclusive-3-NS"

    value: Decimal = field(
        metadata={
            "required": True,
            "max_exclusive": Decimal("171942968603657986"),
        }
    )
