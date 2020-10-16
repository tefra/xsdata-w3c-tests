from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-duration-maxInclusive-1-NS"


@dataclass
class NistschemaSvIvAtomicDurationMaxInclusive1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-duration-maxInclusive-1"
        namespace = "NISTSchema-SV-IV-atomic-duration-maxInclusive-1-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "max_inclusive": "P1970Y01M01DT00H00M00S",
        }
    )
