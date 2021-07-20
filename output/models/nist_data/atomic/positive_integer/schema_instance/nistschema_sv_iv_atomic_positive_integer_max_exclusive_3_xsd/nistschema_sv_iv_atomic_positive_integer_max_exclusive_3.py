from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-positiveInteger-maxExclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicPositiveIntegerMaxExclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-positiveInteger-maxExclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-positiveInteger-maxExclusive-3-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "max_exclusive": 685616415831176051,
        }
    )
