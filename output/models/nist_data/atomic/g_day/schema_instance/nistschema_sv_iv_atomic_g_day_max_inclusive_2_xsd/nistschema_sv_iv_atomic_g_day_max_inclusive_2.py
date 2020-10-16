from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gDay-maxInclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicGDayMaxInclusive2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gDay-maxInclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-gDay-maxInclusive-2-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "max_inclusive": "---07",
        }
    )
