from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-decimal-enumeration-1-NS"


class NistschemaSvIvAtomicDecimalEnumeration1Type(Enum):
    VALUE_0_774 = Decimal("0.774")
    VALUE_885368_72 = Decimal("885368.72")
    VALUE_8_63882452 = Decimal("8.63882452")
    VALUE_MINUS_0_92 = Decimal("-0.92")
    VALUE_549_95 = Decimal("549.95")
    VALUE_MINUS_1914_0 = Decimal("-1914.0")


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDecimalEnumeration1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-decimal-enumeration-1"
        namespace = "NISTSchema-SV-IV-atomic-decimal-enumeration-1-NS"

    value: NistschemaSvIvAtomicDecimalEnumeration1Type = field(
        metadata={
            "required": True,
        }
    )
