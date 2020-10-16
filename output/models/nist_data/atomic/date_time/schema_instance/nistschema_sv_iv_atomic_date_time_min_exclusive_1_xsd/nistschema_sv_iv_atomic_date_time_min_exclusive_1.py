from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-dateTime-minExclusive-1-NS"


@dataclass
class NistschemaSvIvAtomicDateTimeMinExclusive1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-dateTime-minExclusive-1"
        namespace = "NISTSchema-SV-IV-atomic-dateTime-minExclusive-1-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "min_exclusive": "1970-01-01T00:00:00",
        }
    )
