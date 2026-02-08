from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-decimal-enumeration-3-NS"


class NistschemaSvIvAtomicDecimalEnumeration3Type(Enum):
    VALUE_840 = Decimal("840")
    VALUE_MINUS_584_55228 = Decimal("-584.55228")
    VALUE_MINUS_97585886185 = Decimal("-97585886185")
    VALUE_0_672 = Decimal("0.672")
    VALUE_MINUS_75_62365 = Decimal("-75.62365")
    VALUE_MINUS_7_335 = Decimal("-7.335")
    VALUE_0_86054905 = Decimal("0.86054905")
    VALUE_MINUS_5439_8474996 = Decimal("-5439.8474996")


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDecimalEnumeration3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-decimal-enumeration-3"
        namespace = "NISTSchema-SV-IV-atomic-decimal-enumeration-3-NS"

    value: NistschemaSvIvAtomicDecimalEnumeration3Type = field()
