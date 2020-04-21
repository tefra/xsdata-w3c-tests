from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gMonth-pattern-1-NS"


@dataclass
class NistschemaSvIvAtomicGMonthPattern1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gMonth-pattern-1"
        namespace = "NISTSchema-SV-IV-atomic-gMonth-pattern-1-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            pattern=r"--1\d"
        )
    )
