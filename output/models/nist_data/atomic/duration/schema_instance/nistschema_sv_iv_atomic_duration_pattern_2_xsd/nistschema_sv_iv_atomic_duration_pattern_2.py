from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-duration-pattern-2-NS"


@dataclass
class NistschemaSvIvAtomicDurationPattern2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-duration-pattern-2"
        namespace = "NISTSchema-SV-IV-atomic-duration-pattern-2-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "pattern": r"P\d\d74Y0\dM\d6DT1\dH\d0M\d7S",
        }
    )
