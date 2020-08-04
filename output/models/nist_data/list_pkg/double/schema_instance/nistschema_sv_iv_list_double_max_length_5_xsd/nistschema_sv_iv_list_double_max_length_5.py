from decimal import Decimal
from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-double-maxLength-5-NS"


@dataclass
class NistschemaSvIvListDoubleMaxLength5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-double-maxLength-5"
        namespace = "NISTSchema-SV-IV-list-double-maxLength-5-NS"

    value: List[Decimal] = field(
        default_factory=list,
        metadata=dict(
            required=True,
            max_length=10,
            tokens=True
        )
    )
