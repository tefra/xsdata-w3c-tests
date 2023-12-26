from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-nonPositiveInteger-minExclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicNonPositiveIntegerMinExclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-nonPositiveInteger-minExclusive-4"
        namespace = (
            "NISTSchema-SV-IV-atomic-nonPositiveInteger-minExclusive-4-NS"
        )

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
            "min_exclusive": -594976296252018754,
        },
    )
