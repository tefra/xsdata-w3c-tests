from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-nonNegativeInteger-maxExclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicNonNegativeIntegerMaxExclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-nonNegativeInteger-maxExclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-nonNegativeInteger-maxExclusive-3-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "max_exclusive": 278524439385076983,
        }
    )
