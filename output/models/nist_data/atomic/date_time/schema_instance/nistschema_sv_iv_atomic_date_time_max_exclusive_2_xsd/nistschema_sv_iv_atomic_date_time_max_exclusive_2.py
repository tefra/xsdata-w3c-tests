from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-dateTime-maxExclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicDateTimeMaxExclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-dateTime-maxExclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-dateTime-maxExclusive-2-NS"

    value: Optional[datetime] = field(
        default=None,
        metadata={
            "required": True,
            "max_exclusive": datetime(1980, 5, 22, 13, 12, 9),
        }
    )
