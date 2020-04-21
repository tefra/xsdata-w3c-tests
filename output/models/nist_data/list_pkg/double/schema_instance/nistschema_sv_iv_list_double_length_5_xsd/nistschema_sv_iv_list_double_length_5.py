from decimal import Decimal
from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-double-length-5-NS"


@dataclass
class NistschemaSvIvListDoubleLength5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-double-length-5"
        namespace = "NISTSchema-SV-IV-list-double-length-5-NS"

    value: List[Decimal] = field(
        default_factory=list,
        metadata=dict(
            min_occurs=0,
            max_occurs=9223372036854775807,
            length=10
        )
    )
