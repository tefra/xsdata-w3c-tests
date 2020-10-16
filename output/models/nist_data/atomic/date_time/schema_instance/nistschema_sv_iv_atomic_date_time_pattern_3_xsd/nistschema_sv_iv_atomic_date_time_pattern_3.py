from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-dateTime-pattern-3-NS"


@dataclass
class NistschemaSvIvAtomicDateTimePattern3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-dateTime-pattern-3"
        namespace = "NISTSchema-SV-IV-atomic-dateTime-pattern-3-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "pattern": r"19\d\d-0\d-0\dT\d5:1\d:3\d",
        }
    )
