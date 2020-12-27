from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-dateTime-minExclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicDateTimeMinExclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-dateTime-minExclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-dateTime-minExclusive-2-NS"

    value: Optional[datetime] = field(
        default=None,
        metadata={
            "required": True,
            "min_exclusive": datetime(1974, 4, 26, 23, 23, 51),
        }
    )
