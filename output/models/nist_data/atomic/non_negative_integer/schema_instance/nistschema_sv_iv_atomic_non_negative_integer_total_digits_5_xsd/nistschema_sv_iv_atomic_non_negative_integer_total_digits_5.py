from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-nonNegativeInteger-totalDigits-5-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicNonNegativeIntegerTotalDigits5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-nonNegativeInteger-totalDigits-5"
        namespace = (
            "NISTSchema-SV-IV-atomic-nonNegativeInteger-totalDigits-5-NS"
        )

    value: int = field(
        metadata={
            "required": True,
            "total_digits": 18,
        }
    )
