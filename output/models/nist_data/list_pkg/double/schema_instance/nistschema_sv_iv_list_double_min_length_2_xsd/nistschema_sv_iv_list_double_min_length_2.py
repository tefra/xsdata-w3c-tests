from dataclasses import dataclass, field
from decimal import Decimal
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-double-minLength-2-NS"


@dataclass
class NistschemaSvIvListDoubleMinLength2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-double-minLength-2"
        namespace = "NISTSchema-SV-IV-list-double-minLength-2-NS"

    value: List[Decimal] = field(
        default_factory=list,
        metadata=dict(
            required=True,
            min_length=6,
            tokens=True
        )
    )
