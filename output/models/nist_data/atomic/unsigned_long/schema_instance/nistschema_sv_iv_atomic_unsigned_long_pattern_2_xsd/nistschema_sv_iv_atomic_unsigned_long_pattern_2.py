from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedLong-pattern-2-NS"


@dataclass
class NistschemaSvIvAtomicUnsignedLongPattern2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedLong-pattern-2"
        namespace = "NISTSchema-SV-IV-atomic-unsignedLong-pattern-2-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "pattern": r"\d{5}",
        }
    )
