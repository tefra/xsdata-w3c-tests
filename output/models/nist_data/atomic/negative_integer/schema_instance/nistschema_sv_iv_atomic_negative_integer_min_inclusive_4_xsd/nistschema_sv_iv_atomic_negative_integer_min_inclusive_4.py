from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-negativeInteger-minInclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicNegativeIntegerMinInclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-negativeInteger-minInclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-negativeInteger-minInclusive-4-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": -947674826094804355,
        }
    )
