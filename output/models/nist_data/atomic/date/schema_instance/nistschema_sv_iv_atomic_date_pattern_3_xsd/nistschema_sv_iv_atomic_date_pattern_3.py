from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-date-pattern-3-NS"


@dataclass
class NistschemaSvIvAtomicDatePattern3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-date-pattern-3"
        namespace = "NISTSchema-SV-IV-atomic-date-pattern-3-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "pattern": r"\d\d90-\d7-2\d",
        }
    )
