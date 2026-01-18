from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedInt-totalDigits-2-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicUnsignedIntTotalDigits2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedInt-totalDigits-2"
        namespace = "NISTSchema-SV-IV-atomic-unsignedInt-totalDigits-2-NS"

    value: int = field(
        metadata={
            "required": True,
            "total_digits": 3,
        }
    )
