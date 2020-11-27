from dataclasses import dataclass, field
from decimal import Decimal
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-decimal-length-1-NS"


@dataclass
class NistschemaSvIvListDecimalLength1:
    class Meta:
        name = "NISTSchema-SV-IV-list-decimal-length-1"
        namespace = "NISTSchema-SV-IV-list-decimal-length-1-NS"

    value: List[Decimal] = field(
        default_factory=list,
        metadata={
            "required": True,
            "length": 5,
            "tokens": True,
        }
    )
