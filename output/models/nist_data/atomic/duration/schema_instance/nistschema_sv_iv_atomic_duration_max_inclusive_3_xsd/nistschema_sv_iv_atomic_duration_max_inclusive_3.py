from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-duration-maxInclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicDurationMaxInclusive3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-duration-maxInclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-duration-maxInclusive-3-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "max_inclusive": "P1981Y03M20DT22H33M14S",
        }
    )
