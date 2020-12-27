from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-dateTime-minInclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicDateTimeMinInclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-dateTime-minInclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-dateTime-minInclusive-3-NS"

    value: Optional[datetime] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": datetime(1978, 11, 30, 10, 14, 33),
        }
    )
