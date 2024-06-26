from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-nonPositiveInteger-minExclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicNonPositiveIntegerMinExclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-nonPositiveInteger-minExclusive-3"
        namespace = (
            "NISTSchema-SV-IV-atomic-nonPositiveInteger-minExclusive-3-NS"
        )

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
            "min_exclusive": -406392790344449528,
        },
    )
