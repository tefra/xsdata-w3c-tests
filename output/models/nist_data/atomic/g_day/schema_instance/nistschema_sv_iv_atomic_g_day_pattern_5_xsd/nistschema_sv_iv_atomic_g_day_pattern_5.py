from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gDay-pattern-5-NS"


@dataclass
class NistschemaSvIvAtomicGDayPattern5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gDay-pattern-5"
        namespace = "NISTSchema-SV-IV-atomic-gDay-pattern-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "pattern": r"---1\d",
        }
    )
