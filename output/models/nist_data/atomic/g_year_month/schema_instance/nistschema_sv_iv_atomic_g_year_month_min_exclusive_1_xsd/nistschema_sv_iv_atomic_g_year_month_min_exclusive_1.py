from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYearMonth-minExclusive-1-NS"


@dataclass
class NistschemaSvIvAtomicGYearMonthMinExclusive1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYearMonth-minExclusive-1"
        namespace = "NISTSchema-SV-IV-atomic-gYearMonth-minExclusive-1-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "min_exclusive": "1970-01",
        }
    )
