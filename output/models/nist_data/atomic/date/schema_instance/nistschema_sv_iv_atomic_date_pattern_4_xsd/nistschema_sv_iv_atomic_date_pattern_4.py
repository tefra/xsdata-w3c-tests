from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-date-pattern-4-NS"


@dataclass
class NistschemaSvIvAtomicDatePattern4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-date-pattern-4"
        namespace = "NISTSchema-SV-IV-atomic-date-pattern-4-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            pattern=r"17\d\d-\d0-1\d"
        )
    )