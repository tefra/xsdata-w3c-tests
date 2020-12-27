from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-dateTime-minExclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicDateTimeMinExclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-dateTime-minExclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-dateTime-minExclusive-4-NS"

    value: Optional[datetime] = field(
        default=None,
        metadata={
            "required": True,
            "min_exclusive": datetime(2001, 9, 4, 0, 13, 18),
        }
    )
