from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-short-minExclusive-1-NS"


@dataclass
class NistschemaSvIvAtomicShortMinExclusive1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-short-minExclusive-1"
        namespace = "NISTSchema-SV-IV-atomic-short-minExclusive-1-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
            "min_exclusive": -32768,
        },
    )
