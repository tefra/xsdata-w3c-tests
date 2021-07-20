from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-negativeInteger-minExclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicNegativeIntegerMinExclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-negativeInteger-minExclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-negativeInteger-minExclusive-2-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "min_exclusive": -435976618086570511,
        }
    )
