from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-nonPositiveInteger-maxExclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicNonPositiveIntegerMaxExclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-nonPositiveInteger-maxExclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-nonPositiveInteger-maxExclusive-2-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "max_exclusive": -267691436022826633,
        }
    )
