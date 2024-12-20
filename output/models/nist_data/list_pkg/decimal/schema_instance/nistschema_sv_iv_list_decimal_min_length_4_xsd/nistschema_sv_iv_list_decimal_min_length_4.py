from dataclasses import dataclass, field
from decimal import Decimal

__NAMESPACE__ = "NISTSchema-SV-IV-list-decimal-minLength-4-NS"


@dataclass
class NistschemaSvIvListDecimalMinLength4:
    class Meta:
        name = "NISTSchema-SV-IV-list-decimal-minLength-4"
        namespace = "NISTSchema-SV-IV-list-decimal-minLength-4-NS"

    value: list[Decimal] = field(
        default_factory=list,
        metadata={
            "min_length": 8,
            "tokens": True,
        },
    )
