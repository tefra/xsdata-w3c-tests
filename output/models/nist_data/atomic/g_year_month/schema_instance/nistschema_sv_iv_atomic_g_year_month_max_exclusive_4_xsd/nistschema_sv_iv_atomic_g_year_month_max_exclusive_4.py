from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYearMonth-maxExclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicGYearMonthMaxExclusive4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYearMonth-maxExclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-gYearMonth-maxExclusive-4-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            max_exclusive="1981-02"
        )
    )