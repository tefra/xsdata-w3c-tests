from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-date-minExclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicDateMinExclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-date-minExclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-date-minExclusive-2-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "min_exclusive": "2027-03-05",
        }
    )
