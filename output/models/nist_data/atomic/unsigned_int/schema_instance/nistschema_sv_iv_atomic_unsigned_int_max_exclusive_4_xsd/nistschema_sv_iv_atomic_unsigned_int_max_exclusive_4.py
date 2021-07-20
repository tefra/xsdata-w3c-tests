from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedInt-maxExclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicUnsignedIntMaxExclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedInt-maxExclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-unsignedInt-maxExclusive-4-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "max_exclusive": 1033689612,
        }
    )
