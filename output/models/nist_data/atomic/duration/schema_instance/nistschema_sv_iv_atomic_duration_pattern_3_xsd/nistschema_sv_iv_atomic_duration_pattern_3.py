from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-duration-pattern-3-NS"


@dataclass
class NistschemaSvIvAtomicDurationPattern3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-duration-pattern-3"
        namespace = "NISTSchema-SV-IV-atomic-duration-pattern-3-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            pattern=r"P20\d\dY\d3M\d1DT\d4H\d7M\d6S"
        )
    )
