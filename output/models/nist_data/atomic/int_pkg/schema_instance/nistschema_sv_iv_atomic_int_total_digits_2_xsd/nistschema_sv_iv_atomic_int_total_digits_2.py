from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-int-totalDigits-2-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicIntTotalDigits2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-int-totalDigits-2"
        namespace = "NISTSchema-SV-IV-atomic-int-totalDigits-2-NS"

    value: int = field(
        metadata={
            "total_digits": 3,
        }
    )
