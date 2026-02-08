from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-byte-enumeration-3-NS"


class NistschemaSvIvAtomicByteEnumeration3Type(Enum):
    VALUE_60 = 60
    VALUE_62 = 62
    VALUE_5 = 5
    VALUE_MINUS_128 = -128
    VALUE_4 = 4
    VALUE_57 = 57
    VALUE_127 = 127
    VALUE_30 = 30


@dataclass(kw_only=True)
class NistschemaSvIvAtomicByteEnumeration3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-byte-enumeration-3"
        namespace = "NISTSchema-SV-IV-atomic-byte-enumeration-3-NS"

    value: NistschemaSvIvAtomicByteEnumeration3Type = field()
