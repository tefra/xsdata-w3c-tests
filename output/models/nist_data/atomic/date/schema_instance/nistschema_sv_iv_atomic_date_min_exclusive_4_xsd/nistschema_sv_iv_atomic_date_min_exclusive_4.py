from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-date-minExclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicDateMinExclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-date-minExclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-date-minExclusive-4-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "min_exclusive": "2025-01-09",
        }
    )
