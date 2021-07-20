from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-positiveInteger-minInclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicPositiveIntegerMinInclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-positiveInteger-minInclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-positiveInteger-minInclusive-4-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "min_inclusive": 69860014844260743,
        }
    )
