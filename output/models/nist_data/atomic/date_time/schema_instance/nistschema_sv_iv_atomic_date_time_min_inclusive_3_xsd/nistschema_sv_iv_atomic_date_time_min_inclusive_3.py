from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-dateTime-minInclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicDateTimeMinInclusive3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-dateTime-minInclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-dateTime-minInclusive-3-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": "1978-11-30T10:14:33",
        }
    )
