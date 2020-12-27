from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-dateTime-maxInclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicDateTimeMaxInclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-dateTime-maxInclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-dateTime-maxInclusive-2-NS"

    value: Optional[datetime] = field(
        default=None,
        metadata={
            "required": True,
            "max_inclusive": datetime(1982, 5, 22, 18, 1, 37),
        }
    )
