from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-short-maxInclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicShortMaxInclusive2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-short-maxInclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-short-maxInclusive-2-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
            "max_inclusive": 2249,
        }
    )
