from dataclasses import dataclass, field
from decimal import Decimal
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-double-maxLength-1-NS"


@dataclass
class NistschemaSvIvListDoubleMaxLength1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-double-maxLength-1"
        namespace = "NISTSchema-SV-IV-list-double-maxLength-1-NS"

    value: List[Decimal] = field(
        default_factory=list,
        metadata=dict(
            required=True,
            max_length=5,
            tokens=True
        )
    )
