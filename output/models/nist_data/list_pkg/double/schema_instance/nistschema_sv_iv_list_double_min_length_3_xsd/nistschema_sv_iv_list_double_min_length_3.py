from dataclasses import dataclass, field
from decimal import Decimal
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-double-minLength-3-NS"


@dataclass
class NistschemaSvIvListDoubleMinLength3:
    class Meta:
        name = "NISTSchema-SV-IV-list-double-minLength-3"
        namespace = "NISTSchema-SV-IV-list-double-minLength-3-NS"

    value: List[Decimal] = field(
        default_factory=list,
        metadata={
            "required": True,
            "min_length": 7,
            "tokens": True,
        }
    )
