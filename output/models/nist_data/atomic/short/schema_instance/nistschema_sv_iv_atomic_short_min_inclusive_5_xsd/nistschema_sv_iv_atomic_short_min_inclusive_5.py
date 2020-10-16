from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-short-minInclusive-5-NS"


@dataclass
class NistschemaSvIvAtomicShortMinInclusive5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-short-minInclusive-5"
        namespace = "NISTSchema-SV-IV-atomic-short-minInclusive-5-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": 32767,
        }
    )
