from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYear-maxInclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicGYearMaxInclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYear-maxInclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-gYear-maxInclusive-2-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "max_inclusive": "1975",
        }
    )
