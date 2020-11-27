from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-date-minInclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicDateMinInclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-date-minInclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-date-minInclusive-2-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": "1973-09-08",
        }
    )
