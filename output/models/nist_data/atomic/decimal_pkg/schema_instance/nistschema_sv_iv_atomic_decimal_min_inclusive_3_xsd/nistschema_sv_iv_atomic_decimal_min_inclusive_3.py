from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-decimal-minInclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicDecimalMinInclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-decimal-minInclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-decimal-minInclusive-3-NS"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": Decimal("-785368448026986020"),
        }
    )
