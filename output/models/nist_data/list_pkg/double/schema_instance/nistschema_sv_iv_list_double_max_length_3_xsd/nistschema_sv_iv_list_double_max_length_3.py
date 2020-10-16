from dataclasses import dataclass, field
from decimal import Decimal
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-double-maxLength-3-NS"


@dataclass
class NistschemaSvIvListDoubleMaxLength3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-double-maxLength-3"
        namespace = "NISTSchema-SV-IV-list-double-maxLength-3-NS"

    value: List[Decimal] = field(
        default_factory=list,
        metadata={
            "required": True,
            "max_length": 7,
            "tokens": True,
        }
    )
