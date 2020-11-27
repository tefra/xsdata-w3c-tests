from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-date-minExclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicDateMinExclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-date-minExclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-date-minExclusive-3-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "min_exclusive": "2005-11-17",
        }
    )
