from decimal import Decimal
from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-decimal-length-4-NS"


@dataclass
class NistschemaSvIvListDecimalLength4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-decimal-length-4"
        namespace = "NISTSchema-SV-IV-list-decimal-length-4-NS"

    value: List[Decimal] = field(
        default_factory=list,
        metadata=dict(
            min_occurs=0,
            max_occurs=9223372036854775807,
            length=8
        )
    )
