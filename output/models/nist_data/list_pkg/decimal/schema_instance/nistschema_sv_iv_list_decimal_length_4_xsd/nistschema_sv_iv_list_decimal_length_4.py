from dataclasses import dataclass, field
from decimal import Decimal
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-decimal-length-4-NS"


@dataclass
class NistschemaSvIvListDecimalLength4:
    class Meta:
        name = "NISTSchema-SV-IV-list-decimal-length-4"
        namespace = "NISTSchema-SV-IV-list-decimal-length-4-NS"

    value: List[Decimal] = field(
        default_factory=list,
        metadata={
            "length": 8,
            "tokens": True,
        },
    )
