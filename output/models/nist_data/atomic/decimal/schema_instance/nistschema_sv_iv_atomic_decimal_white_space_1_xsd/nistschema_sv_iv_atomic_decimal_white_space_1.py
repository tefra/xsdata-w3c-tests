from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-decimal-whiteSpace-1-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDecimalWhiteSpace1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-decimal-whiteSpace-1"
        namespace = "NISTSchema-SV-IV-atomic-decimal-whiteSpace-1-NS"

    value: Decimal = field(
        metadata={
            "required": True,
            "white_space": "collapse",
        }
    )
