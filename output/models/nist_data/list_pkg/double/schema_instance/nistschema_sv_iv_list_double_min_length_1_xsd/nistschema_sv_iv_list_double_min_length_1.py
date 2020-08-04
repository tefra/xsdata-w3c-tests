from decimal import Decimal
from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-double-minLength-1-NS"


@dataclass
class NistschemaSvIvListDoubleMinLength1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-double-minLength-1"
        namespace = "NISTSchema-SV-IV-list-double-minLength-1-NS"

    value: List[Decimal] = field(
        default_factory=list,
        metadata=dict(
            required=True,
            min_length=5,
            tokens=True
        )
    )
