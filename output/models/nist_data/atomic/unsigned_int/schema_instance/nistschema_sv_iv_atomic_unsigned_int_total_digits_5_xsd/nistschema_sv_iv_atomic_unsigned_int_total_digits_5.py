from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedInt-totalDigits-5-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicUnsignedIntTotalDigits5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedInt-totalDigits-5"
        namespace = "NISTSchema-SV-IV-atomic-unsignedInt-totalDigits-5-NS"

    value: int = field(
        metadata={
            "required": True,
            "total_digits": 10,
        }
    )
