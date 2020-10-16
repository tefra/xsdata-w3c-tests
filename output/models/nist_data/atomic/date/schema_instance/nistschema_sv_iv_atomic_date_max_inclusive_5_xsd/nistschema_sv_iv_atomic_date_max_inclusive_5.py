from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-date-maxInclusive-5-NS"


@dataclass
class NistschemaSvIvAtomicDateMaxInclusive5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-date-maxInclusive-5"
        namespace = "NISTSchema-SV-IV-atomic-date-maxInclusive-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "max_inclusive": "2030-12-31",
        }
    )
