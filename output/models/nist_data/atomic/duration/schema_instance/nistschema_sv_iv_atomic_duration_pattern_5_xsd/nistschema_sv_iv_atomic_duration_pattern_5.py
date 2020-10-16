from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-duration-pattern-5-NS"


@dataclass
class NistschemaSvIvAtomicDurationPattern5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-duration-pattern-5"
        namespace = "NISTSchema-SV-IV-atomic-duration-pattern-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "pattern": r"P\d\d63Y\d4M1\dDT0\dH\d4M4\dS",
        }
    )
