from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-dateTime-maxInclusive-5-NS"


@dataclass
class NistschemaSvIvAtomicDateTimeMaxInclusive5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-dateTime-maxInclusive-5"
        namespace = "NISTSchema-SV-IV-atomic-dateTime-maxInclusive-5-NS"

    value: Optional[datetime] = field(
        default=None,
        metadata={
            "required": True,
            "max_inclusive": datetime(2030, 12, 31, 23, 59, 59),
        }
    )
