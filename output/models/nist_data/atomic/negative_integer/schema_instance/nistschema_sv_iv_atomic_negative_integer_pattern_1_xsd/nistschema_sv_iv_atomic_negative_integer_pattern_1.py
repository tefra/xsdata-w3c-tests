from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-negativeInteger-pattern-1-NS"


@dataclass
class NistschemaSvIvAtomicNegativeIntegerPattern1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-negativeInteger-pattern-1"
        namespace = "NISTSchema-SV-IV-atomic-negativeInteger-pattern-1-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "pattern": r"\-\d{1}",
        }
    )
