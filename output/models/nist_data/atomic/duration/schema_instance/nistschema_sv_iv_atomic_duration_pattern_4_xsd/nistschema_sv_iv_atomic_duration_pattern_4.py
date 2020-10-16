from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-duration-pattern-4-NS"


@dataclass
class NistschemaSvIvAtomicDurationPattern4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-duration-pattern-4"
        namespace = "NISTSchema-SV-IV-atomic-duration-pattern-4-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "pattern": r"P19\d\dY\d8M\d3DT\d0H1\dM\d2S",
        }
    )
