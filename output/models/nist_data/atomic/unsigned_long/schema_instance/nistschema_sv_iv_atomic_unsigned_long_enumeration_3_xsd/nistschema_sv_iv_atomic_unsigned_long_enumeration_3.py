from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedLong-enumeration-3-NS"


class NistschemaSvIvAtomicUnsignedLongEnumeration3Type(Enum):
    VALUE_760056434 = 760056434
    VALUE_33505897371058979 = 33505897371058979
    VALUE_38 = 38
    VALUE_492728752144644066 = 492728752144644066
    VALUE_7037409938820924 = 7037409938820924
    VALUE_51135955 = 51135955
    VALUE_48185 = 48185
    VALUE_5876730603 = 5876730603


@dataclass(kw_only=True)
class NistschemaSvIvAtomicUnsignedLongEnumeration3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedLong-enumeration-3"
        namespace = "NISTSchema-SV-IV-atomic-unsignedLong-enumeration-3-NS"

    value: NistschemaSvIvAtomicUnsignedLongEnumeration3Type = field()
