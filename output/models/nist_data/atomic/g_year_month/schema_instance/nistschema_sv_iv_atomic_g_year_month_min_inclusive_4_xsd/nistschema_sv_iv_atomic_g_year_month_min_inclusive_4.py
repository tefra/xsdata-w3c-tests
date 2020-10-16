from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYearMonth-minInclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicGYearMonthMinInclusive4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYearMonth-minInclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-gYearMonth-minInclusive-4-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": "1988-05",
        }
    )
