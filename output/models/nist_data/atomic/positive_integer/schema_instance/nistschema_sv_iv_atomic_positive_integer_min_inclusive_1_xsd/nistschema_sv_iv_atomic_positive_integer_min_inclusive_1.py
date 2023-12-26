from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-positiveInteger-minInclusive-1-NS"


@dataclass
class NistschemaSvIvAtomicPositiveIntegerMinInclusive1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-positiveInteger-minInclusive-1"
        namespace = "NISTSchema-SV-IV-atomic-positiveInteger-minInclusive-1-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": 1,
        },
    )
