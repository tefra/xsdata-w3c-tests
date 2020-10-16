from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gDay-pattern-3-NS"


@dataclass
class NistschemaSvIvAtomicGDayPattern3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gDay-pattern-3"
        namespace = "NISTSchema-SV-IV-atomic-gDay-pattern-3-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "pattern": r"---0\d",
        }
    )
