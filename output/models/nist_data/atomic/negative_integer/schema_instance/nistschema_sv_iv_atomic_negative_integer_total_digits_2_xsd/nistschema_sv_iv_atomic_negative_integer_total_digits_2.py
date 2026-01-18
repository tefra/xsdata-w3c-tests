from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-negativeInteger-totalDigits-2-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicNegativeIntegerTotalDigits2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-negativeInteger-totalDigits-2"
        namespace = "NISTSchema-SV-IV-atomic-negativeInteger-totalDigits-2-NS"

    value: int = field(
        metadata={
            "required": True,
            "total_digits": 5,
        }
    )
