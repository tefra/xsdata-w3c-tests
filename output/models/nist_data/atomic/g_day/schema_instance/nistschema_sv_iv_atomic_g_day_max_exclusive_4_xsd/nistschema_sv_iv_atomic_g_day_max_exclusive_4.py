from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gDay-maxExclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicGDayMaxExclusive4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gDay-maxExclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-gDay-maxExclusive-4-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "max_exclusive": "---15",
        }
    )
