from decimal import Decimal
from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-decimal-maxLength-3-NS"


@dataclass
class NistschemaSvIvListDecimalMaxLength3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-decimal-maxLength-3"
        namespace = "NISTSchema-SV-IV-list-decimal-maxLength-3-NS"

    value: List[Decimal] = field(
        default_factory=list,
        metadata=dict(
            min_occurs=0,
            max_occurs=9223372036854775807,
            max_length=7
        )
    )
