from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-short-fractionDigits-1-NS"


@dataclass
class NistschemaSvIvAtomicShortFractionDigits1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-short-fractionDigits-1"
        namespace = "NISTSchema-SV-IV-atomic-short-fractionDigits-1-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
            "fraction_digits": 0,
        },
    )
