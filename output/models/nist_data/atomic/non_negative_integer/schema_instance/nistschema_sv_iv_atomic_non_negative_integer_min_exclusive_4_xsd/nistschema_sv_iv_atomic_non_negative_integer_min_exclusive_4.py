from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-nonNegativeInteger-minExclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicNonNegativeIntegerMinExclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-nonNegativeInteger-minExclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-nonNegativeInteger-minExclusive-4-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "min_exclusive": 656186311861347125,
        }
    )
