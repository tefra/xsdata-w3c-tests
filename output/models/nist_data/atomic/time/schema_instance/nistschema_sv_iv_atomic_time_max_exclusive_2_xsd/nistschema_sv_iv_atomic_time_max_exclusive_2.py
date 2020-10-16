from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-time-maxExclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicTimeMaxExclusive2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-time-maxExclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-time-maxExclusive-2-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "max_exclusive": "08:19:11",
        }
    )
