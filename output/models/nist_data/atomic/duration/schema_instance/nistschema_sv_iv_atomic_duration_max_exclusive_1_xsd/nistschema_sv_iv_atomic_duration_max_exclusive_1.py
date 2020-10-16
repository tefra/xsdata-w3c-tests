from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-duration-maxExclusive-1-NS"


@dataclass
class NistschemaSvIvAtomicDurationMaxExclusive1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-duration-maxExclusive-1"
        namespace = "NISTSchema-SV-IV-atomic-duration-maxExclusive-1-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "max_exclusive": "P1970Y01M01DT00H00M01S",
        }
    )
