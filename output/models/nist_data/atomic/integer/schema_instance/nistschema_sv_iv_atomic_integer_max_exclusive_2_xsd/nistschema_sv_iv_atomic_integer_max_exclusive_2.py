from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-integer-maxExclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicIntegerMaxExclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-integer-maxExclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-integer-maxExclusive-2-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
            "max_exclusive": -863230876206589446,
        }
    )
