from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-dateTime-minInclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicDateTimeMinInclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-dateTime-minInclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-dateTime-minInclusive-2-NS"

    value: Optional[datetime] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": datetime(1972, 10, 10, 11, 7, 3),
        }
    )
