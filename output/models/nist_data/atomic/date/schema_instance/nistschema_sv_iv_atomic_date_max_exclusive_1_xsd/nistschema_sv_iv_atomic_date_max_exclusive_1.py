from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-date-maxExclusive-1-NS"


@dataclass
class NistschemaSvIvAtomicDateMaxExclusive1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-date-maxExclusive-1"
        namespace = "NISTSchema-SV-IV-atomic-date-maxExclusive-1-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "max_exclusive": "1970-01-02",
        }
    )
