from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYearMonth-pattern-3-NS"


@dataclass
class NistschemaSvIvAtomicGYearMonthPattern3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYearMonth-pattern-3"
        namespace = "NISTSchema-SV-IV-atomic-gYearMonth-pattern-3-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            pattern=r"\d\d76-0\d"
        )
    )