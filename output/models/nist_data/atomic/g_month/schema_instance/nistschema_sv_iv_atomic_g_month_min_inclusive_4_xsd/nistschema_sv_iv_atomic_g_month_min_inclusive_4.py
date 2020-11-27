from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gMonth-minInclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicGMonthMinInclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gMonth-minInclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-gMonth-minInclusive-4-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": "--11",
        }
    )
