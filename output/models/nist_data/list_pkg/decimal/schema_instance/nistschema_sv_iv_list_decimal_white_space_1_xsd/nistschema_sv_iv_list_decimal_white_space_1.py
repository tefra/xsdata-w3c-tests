from dataclasses import dataclass, field
from decimal import Decimal

__NAMESPACE__ = "NISTSchema-SV-IV-list-decimal-whiteSpace-1-NS"


@dataclass
class NistschemaSvIvListDecimalWhiteSpace1:
    class Meta:
        name = "NISTSchema-SV-IV-list-decimal-whiteSpace-1"
        namespace = "NISTSchema-SV-IV-list-decimal-whiteSpace-1-NS"

    value: list[Decimal] = field(
        default_factory=list,
        metadata={
            "white_space": "collapse",
            "tokens": True,
        },
    )
