from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gMonth-pattern-2-NS"


@dataclass
class NistschemaSvIvAtomicGMonthPattern2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gMonth-pattern-2"
        namespace = "NISTSchema-SV-IV-atomic-gMonth-pattern-2-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            pattern=r"--\d2"
        )
    )