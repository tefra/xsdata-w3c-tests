from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-int-maxExclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicIntMaxExclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-int-maxExclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-int-maxExclusive-3-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "max_exclusive": 1403226675,
        }
    )
