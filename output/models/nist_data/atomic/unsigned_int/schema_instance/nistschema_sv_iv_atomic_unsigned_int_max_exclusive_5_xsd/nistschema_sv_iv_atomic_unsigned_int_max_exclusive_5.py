from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedInt-maxExclusive-5-NS"


@dataclass
class NistschemaSvIvAtomicUnsignedIntMaxExclusive5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedInt-maxExclusive-5"
        namespace = "NISTSchema-SV-IV-atomic-unsignedInt-maxExclusive-5-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
            "max_exclusive": 4294967295,
        },
    )
