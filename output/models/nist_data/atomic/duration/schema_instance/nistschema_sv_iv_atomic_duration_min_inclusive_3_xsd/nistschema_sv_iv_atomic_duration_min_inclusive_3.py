from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-duration-minInclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicDurationMinInclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-duration-minInclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-duration-minInclusive-3-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": "P1989Y09M10DT10H34M11S",
        }
    )
