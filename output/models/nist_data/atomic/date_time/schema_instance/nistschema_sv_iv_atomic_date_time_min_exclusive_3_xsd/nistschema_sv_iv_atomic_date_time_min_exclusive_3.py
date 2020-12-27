from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-dateTime-minExclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicDateTimeMinExclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-dateTime-minExclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-dateTime-minExclusive-3-NS"

    value: Optional[datetime] = field(
        default=None,
        metadata={
            "required": True,
            "min_exclusive": datetime(1981, 6, 8, 6, 29, 37),
        }
    )
