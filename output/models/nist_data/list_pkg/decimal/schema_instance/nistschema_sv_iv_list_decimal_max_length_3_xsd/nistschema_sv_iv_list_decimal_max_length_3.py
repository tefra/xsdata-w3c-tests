from dataclasses import dataclass, field
from decimal import Decimal

__NAMESPACE__ = "NISTSchema-SV-IV-list-decimal-maxLength-3-NS"


@dataclass
class NistschemaSvIvListDecimalMaxLength3:
    class Meta:
        name = "NISTSchema-SV-IV-list-decimal-maxLength-3"
        namespace = "NISTSchema-SV-IV-list-decimal-maxLength-3-NS"

    value: list[Decimal] = field(
        default_factory=list,
        metadata={
            "max_length": 7,
            "tokens": True,
        },
    )
