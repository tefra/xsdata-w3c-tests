from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-decimal-whiteSpace-1-NS"


@dataclass
class NistschemaSvIvAtomicDecimalWhiteSpace1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-decimal-whiteSpace-1"
        namespace = "NISTSchema-SV-IV-atomic-decimal-whiteSpace-1-NS"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
            "white_space": "collapse",
        }
    )
