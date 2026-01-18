from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-decimal-enumeration-2-NS"


class NistschemaSvIvAtomicDecimalEnumeration2Type(Enum):
    VALUE_89_20902289982400 = Decimal("89.20902289982400")
    VALUE_729089_6 = Decimal("729089.6")
    VALUE_108747_8431 = Decimal("108747.8431")
    VALUE_89_98169071278 = Decimal("89.98169071278")
    VALUE_8_843008676 = Decimal("8.843008676")
    VALUE_7_682949472786 = Decimal("7.682949472786")
    VALUE_31588397646362_1 = Decimal("31588397646362.1")
    VALUE_MINUS_61113534938_0 = Decimal("-61113534938.0")
    VALUE_0_575 = Decimal("0.575")


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDecimalEnumeration2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-decimal-enumeration-2"
        namespace = "NISTSchema-SV-IV-atomic-decimal-enumeration-2-NS"

    value: NistschemaSvIvAtomicDecimalEnumeration2Type = field(
        metadata={
            "required": True,
        }
    )
