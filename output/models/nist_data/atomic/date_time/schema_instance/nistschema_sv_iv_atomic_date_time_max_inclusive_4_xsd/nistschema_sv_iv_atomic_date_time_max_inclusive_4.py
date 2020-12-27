from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-dateTime-maxInclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicDateTimeMaxInclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-dateTime-maxInclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-dateTime-maxInclusive-4-NS"

    value: Optional[datetime] = field(
        default=None,
        metadata={
            "required": True,
            "max_inclusive": datetime(1972, 9, 29, 19, 51, 19),
        }
    )
