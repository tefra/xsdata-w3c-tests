from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-long-maxExclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicLongMaxExclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-long-maxExclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-long-maxExclusive-2-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
            "max_exclusive": -562908107193849537,
        }
    )
