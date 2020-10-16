from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gMonth-minInclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicGMonthMinInclusive2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gMonth-minInclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-gMonth-minInclusive-2-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": "--05",
        }
    )
