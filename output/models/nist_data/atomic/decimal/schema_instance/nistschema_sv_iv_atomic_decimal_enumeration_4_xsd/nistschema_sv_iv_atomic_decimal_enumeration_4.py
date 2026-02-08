from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-decimal-enumeration-4-NS"


class NistschemaSvIvAtomicDecimalEnumeration4Type(Enum):
    VALUE_613_87 = Decimal("613.87")
    VALUE_1906433845_89 = Decimal("1906433845.89")
    VALUE_MINUS_2_39446916113 = Decimal("-2.39446916113")
    VALUE_MINUS_5286034_1 = Decimal("-5286034.1")
    VALUE_8838363181_0150 = Decimal("8838363181.0150")


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDecimalEnumeration4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-decimal-enumeration-4"
        namespace = "NISTSchema-SV-IV-atomic-decimal-enumeration-4-NS"

    value: NistschemaSvIvAtomicDecimalEnumeration4Type = field()
