from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-date-minExclusive-1-NS"


@dataclass
class NistschemaSvIvAtomicDateMinExclusive1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-date-minExclusive-1"
        namespace = "NISTSchema-SV-IV-atomic-date-minExclusive-1-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "min_exclusive": "1970-01-01",
        }
    )
