from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-decimal-maxExclusive-2-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDecimalMaxExclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-decimal-maxExclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-decimal-maxExclusive-2-NS"

    value: Decimal = field(
        metadata={
            "required": True,
            "max_exclusive": Decimal("78119693427168402"),
        }
    )
