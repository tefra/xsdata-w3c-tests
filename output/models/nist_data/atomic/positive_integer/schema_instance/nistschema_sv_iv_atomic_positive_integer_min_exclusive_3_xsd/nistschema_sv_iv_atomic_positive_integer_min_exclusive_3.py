from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-positiveInteger-minExclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicPositiveIntegerMinExclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-positiveInteger-minExclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-positiveInteger-minExclusive-3-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
            "min_exclusive": 173303931811171541,
        },
    )
