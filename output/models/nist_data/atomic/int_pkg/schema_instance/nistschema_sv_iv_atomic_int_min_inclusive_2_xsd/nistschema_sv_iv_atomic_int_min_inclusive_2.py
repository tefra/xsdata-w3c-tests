from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-int-minInclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicIntMinInclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-int-minInclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-int-minInclusive-2-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": -1728117668,
        },
    )
