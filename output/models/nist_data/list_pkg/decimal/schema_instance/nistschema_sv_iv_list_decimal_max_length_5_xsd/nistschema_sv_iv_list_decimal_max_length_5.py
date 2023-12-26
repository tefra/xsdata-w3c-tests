from dataclasses import dataclass, field
from decimal import Decimal
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-decimal-maxLength-5-NS"


@dataclass
class NistschemaSvIvListDecimalMaxLength5:
    class Meta:
        name = "NISTSchema-SV-IV-list-decimal-maxLength-5"
        namespace = "NISTSchema-SV-IV-list-decimal-maxLength-5-NS"

    value: List[Decimal] = field(
        default_factory=list,
        metadata={
            "max_length": 10,
            "tokens": True,
        },
    )
