from dataclasses import dataclass, field
from decimal import Decimal
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-decimal-minLength-1-NS"


@dataclass
class NistschemaSvIvListDecimalMinLength1:
    class Meta:
        name = "NISTSchema-SV-IV-list-decimal-minLength-1"
        namespace = "NISTSchema-SV-IV-list-decimal-minLength-1-NS"

    value: List[Decimal] = field(
        default_factory=list,
        metadata={
            "min_length": 5,
            "tokens": True,
        },
    )
