from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-time-pattern-3-NS"


@dataclass
class NistschemaSvIvAtomicTimePattern3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-time-pattern-3"
        namespace = "NISTSchema-SV-IV-atomic-time-pattern-3-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            pattern=r"1\d:3\d:\d5"
        )
    )