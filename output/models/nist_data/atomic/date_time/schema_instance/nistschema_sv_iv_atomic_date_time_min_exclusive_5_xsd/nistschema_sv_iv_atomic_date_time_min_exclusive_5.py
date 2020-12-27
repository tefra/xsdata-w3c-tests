from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-dateTime-minExclusive-5-NS"


@dataclass
class NistschemaSvIvAtomicDateTimeMinExclusive5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-dateTime-minExclusive-5"
        namespace = "NISTSchema-SV-IV-atomic-dateTime-minExclusive-5-NS"

    value: Optional[datetime] = field(
        default=None,
        metadata={
            "required": True,
            "min_exclusive": datetime(2030, 12, 31, 23, 59, 58),
        }
    )
