from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-dateTime-minInclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicDateTimeMinInclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-dateTime-minInclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-dateTime-minInclusive-4-NS"

    value: Optional[datetime] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": datetime(2006, 7, 21, 1, 32, 21),
        }
    )
