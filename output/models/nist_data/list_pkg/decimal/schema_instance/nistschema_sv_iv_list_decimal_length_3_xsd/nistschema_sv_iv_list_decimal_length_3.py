from dataclasses import dataclass, field
from decimal import Decimal
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-decimal-length-3-NS"


@dataclass
class NistschemaSvIvListDecimalLength3:
    class Meta:
        name = "NISTSchema-SV-IV-list-decimal-length-3"
        namespace = "NISTSchema-SV-IV-list-decimal-length-3-NS"

    value: List[Decimal] = field(
        default_factory=list,
        metadata={
            "length": 7,
            "tokens": True,
        },
    )
