from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedLong-enumeration-1-NS"


class NistschemaSvIvAtomicUnsignedLongEnumeration1Type(Enum):
    VALUE_235157797394 = 235157797394
    VALUE_2841737 = 2841737
    VALUE_6246890837920823 = 6246890837920823
    VALUE_502437096339080 = 502437096339080
    VALUE_475868893660 = 475868893660
    VALUE_69228431818957325 = 69228431818957325
    VALUE_16 = 16


@dataclass(kw_only=True)
class NistschemaSvIvAtomicUnsignedLongEnumeration1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedLong-enumeration-1"
        namespace = "NISTSchema-SV-IV-atomic-unsignedLong-enumeration-1-NS"

    value: NistschemaSvIvAtomicUnsignedLongEnumeration1Type = field()
