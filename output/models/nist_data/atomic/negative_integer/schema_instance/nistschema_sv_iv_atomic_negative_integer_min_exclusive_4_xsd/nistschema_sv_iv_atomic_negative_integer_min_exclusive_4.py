from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-negativeInteger-minExclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicNegativeIntegerMinExclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-negativeInteger-minExclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-negativeInteger-minExclusive-4-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
            "min_exclusive": -495295756372066909,
        }
    )
