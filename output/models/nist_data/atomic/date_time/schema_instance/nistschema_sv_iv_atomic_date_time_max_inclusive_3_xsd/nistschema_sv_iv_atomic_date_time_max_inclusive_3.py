from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-dateTime-maxInclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicDateTimeMaxInclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-dateTime-maxInclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-dateTime-maxInclusive-3-NS"

    value: Optional[datetime] = field(
        default=None,
        metadata={
            "required": True,
            "max_inclusive": datetime(2003, 3, 9, 2, 0, 23),
        }
    )
