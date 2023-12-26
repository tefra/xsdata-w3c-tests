from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-decimal-enumeration-5-NS"


class NistschemaSvIvAtomicDecimalEnumeration5Type(Enum):
    VALUE_856_89 = Decimal("856.89")
    VALUE_6_9307231814179 = Decimal("6.9307231814179")
    VALUE_MINUS_150 = Decimal("-150")
    VALUE_337920_941 = Decimal("337920.941")
    VALUE_0_3316 = Decimal("0.3316")
    VALUE_MINUS_82_78605057 = Decimal("-82.78605057")
    VALUE_MINUS_0_61 = Decimal("-0.61")


@dataclass
class NistschemaSvIvAtomicDecimalEnumeration5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-decimal-enumeration-5"
        namespace = "NISTSchema-SV-IV-atomic-decimal-enumeration-5-NS"

    value: Optional[NistschemaSvIvAtomicDecimalEnumeration5Type] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
