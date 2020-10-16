from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-short-maxExclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicShortMaxExclusive4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-short-maxExclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-short-maxExclusive-4-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
            "max_exclusive": 21269,
        }
    )
