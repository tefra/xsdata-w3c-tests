from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-duration-minInclusive-1-NS"


@dataclass
class NistschemaSvIvAtomicDurationMinInclusive1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-duration-minInclusive-1"
        namespace = "NISTSchema-SV-IV-atomic-duration-minInclusive-1-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": "P1970Y01M01DT00H00M00S",
        }
    )
