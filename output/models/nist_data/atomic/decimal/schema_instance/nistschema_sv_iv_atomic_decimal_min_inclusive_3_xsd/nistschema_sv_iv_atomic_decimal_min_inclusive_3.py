from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-decimal-minInclusive-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDecimalMinInclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-decimal-minInclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-decimal-minInclusive-3-NS"

    value: Decimal = field(
        metadata={
            "required": True,
            "min_inclusive": Decimal("-785368448026986020"),
        }
    )
