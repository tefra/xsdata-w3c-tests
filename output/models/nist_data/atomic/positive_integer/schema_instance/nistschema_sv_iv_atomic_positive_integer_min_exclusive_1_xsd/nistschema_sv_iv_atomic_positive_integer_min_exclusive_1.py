from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-positiveInteger-minExclusive-1-NS"


@dataclass
class NistschemaSvIvAtomicPositiveIntegerMinExclusive1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-positiveInteger-minExclusive-1"
        namespace = "NISTSchema-SV-IV-atomic-positiveInteger-minExclusive-1-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "min_exclusive": 1,
        }
    )
