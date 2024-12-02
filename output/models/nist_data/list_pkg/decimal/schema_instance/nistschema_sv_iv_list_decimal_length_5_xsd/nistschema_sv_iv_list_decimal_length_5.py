from dataclasses import dataclass, field
from decimal import Decimal

__NAMESPACE__ = "NISTSchema-SV-IV-list-decimal-length-5-NS"


@dataclass
class NistschemaSvIvListDecimalLength5:
    class Meta:
        name = "NISTSchema-SV-IV-list-decimal-length-5"
        namespace = "NISTSchema-SV-IV-list-decimal-length-5-NS"

    value: list[Decimal] = field(
        default_factory=list,
        metadata={
            "length": 10,
            "tokens": True,
        },
    )
