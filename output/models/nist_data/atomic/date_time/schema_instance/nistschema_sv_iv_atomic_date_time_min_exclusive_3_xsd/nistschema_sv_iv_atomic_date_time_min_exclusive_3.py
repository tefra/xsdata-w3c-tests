from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-dateTime-minExclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicDateTimeMinExclusive3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-dateTime-minExclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-dateTime-minExclusive-3-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "min_exclusive": "1981-06-08T06:29:37",
        }
    )
