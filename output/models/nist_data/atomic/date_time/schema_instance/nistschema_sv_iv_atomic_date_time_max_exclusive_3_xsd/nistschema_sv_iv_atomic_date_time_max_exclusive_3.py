from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-dateTime-maxExclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicDateTimeMaxExclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-dateTime-maxExclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-dateTime-maxExclusive-3-NS"

    value: Optional[datetime] = field(
        default=None,
        metadata={
            "required": True,
            "max_exclusive": datetime(1996, 8, 13, 0, 44, 39),
        }
    )
