from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gMonth-minInclusive-1-NS"


@dataclass
class NistschemaSvIvAtomicGMonthMinInclusive1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gMonth-minInclusive-1"
        namespace = "NISTSchema-SV-IV-atomic-gMonth-minInclusive-1-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": "--01",
        }
    )
