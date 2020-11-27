from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-dateTime-maxInclusive-1-NS"


@dataclass
class NistschemaSvIvAtomicDateTimeMaxInclusive1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-dateTime-maxInclusive-1"
        namespace = "NISTSchema-SV-IV-atomic-dateTime-maxInclusive-1-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "max_inclusive": "1970-01-01T00:00:00",
        }
    )
