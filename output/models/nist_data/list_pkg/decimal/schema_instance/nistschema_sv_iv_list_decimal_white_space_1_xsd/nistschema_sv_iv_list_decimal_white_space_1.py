from dataclasses import dataclass, field
from decimal import Decimal
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-decimal-whiteSpace-1-NS"


@dataclass
class NistschemaSvIvListDecimalWhiteSpace1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-decimal-whiteSpace-1"
        namespace = "NISTSchema-SV-IV-list-decimal-whiteSpace-1-NS"

    value: List[Decimal] = field(
        default_factory=list,
        metadata=dict(
            required=True,
            white_space="collapse",
            tokens=True
        )
    )
