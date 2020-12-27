from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-dateTime-maxExclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicDateTimeMaxExclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-dateTime-maxExclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-dateTime-maxExclusive-4-NS"

    value: Optional[datetime] = field(
        default=None,
        metadata={
            "required": True,
            "max_exclusive": datetime(2018, 6, 17, 15, 34, 43),
        }
    )
