from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-duration-minExclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicDurationMinExclusive4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-duration-minExclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-duration-minExclusive-4-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "min_exclusive": "P2029Y10M29DT21H06M18S",
        }
    )
