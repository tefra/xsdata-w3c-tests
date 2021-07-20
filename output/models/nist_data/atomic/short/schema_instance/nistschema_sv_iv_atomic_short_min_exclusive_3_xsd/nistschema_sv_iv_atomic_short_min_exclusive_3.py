from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-short-minExclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicShortMinExclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-short-minExclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-short-minExclusive-3-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "min_exclusive": -20001,
        }
    )
