from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-gYearMonth-whiteSpace-1-NS"


@dataclass
class NistschemaSvIvListGYearMonthWhiteSpace1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-gYearMonth-whiteSpace-1"
        namespace = "NISTSchema-SV-IV-list-gYearMonth-whiteSpace-1-NS"

    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            required=True,
            white_space="collapse",
            tokens=True
        )
    )
