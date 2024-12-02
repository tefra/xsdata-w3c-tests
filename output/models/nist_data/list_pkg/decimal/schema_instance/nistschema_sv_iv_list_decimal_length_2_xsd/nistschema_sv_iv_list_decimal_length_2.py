from dataclasses import dataclass, field
from decimal import Decimal

__NAMESPACE__ = "NISTSchema-SV-IV-list-decimal-length-2-NS"


@dataclass
class NistschemaSvIvListDecimalLength2:
    class Meta:
        name = "NISTSchema-SV-IV-list-decimal-length-2"
        namespace = "NISTSchema-SV-IV-list-decimal-length-2-NS"

    value: list[Decimal] = field(
        default_factory=list,
        metadata={
            "length": 6,
            "tokens": True,
        },
    )
