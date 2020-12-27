from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-dateTime-minInclusive-1-NS"


@dataclass
class NistschemaSvIvAtomicDateTimeMinInclusive1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-dateTime-minInclusive-1"
        namespace = "NISTSchema-SV-IV-atomic-dateTime-minInclusive-1-NS"

    value: Optional[datetime] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": datetime(1970, 1, 1, 0, 0),
        }
    )
