from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-negativeInteger-maxExclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicNegativeIntegerMaxExclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-negativeInteger-maxExclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-negativeInteger-maxExclusive-3-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
            "max_exclusive": -184935339155753553,
        }
    )
