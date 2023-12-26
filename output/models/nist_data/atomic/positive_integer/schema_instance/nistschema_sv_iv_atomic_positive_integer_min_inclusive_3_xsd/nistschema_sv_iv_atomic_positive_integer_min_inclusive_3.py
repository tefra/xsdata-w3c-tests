from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-positiveInteger-minInclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicPositiveIntegerMinInclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-positiveInteger-minInclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-positiveInteger-minInclusive-3-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": 828758841369869991,
        },
    )
