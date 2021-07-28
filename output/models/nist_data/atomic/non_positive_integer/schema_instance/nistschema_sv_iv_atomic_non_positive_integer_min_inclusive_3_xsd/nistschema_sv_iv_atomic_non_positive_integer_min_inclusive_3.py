from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-nonPositiveInteger-minInclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicNonPositiveIntegerMinInclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-nonPositiveInteger-minInclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-nonPositiveInteger-minInclusive-3-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": -214379312213180406,
        }
    )
