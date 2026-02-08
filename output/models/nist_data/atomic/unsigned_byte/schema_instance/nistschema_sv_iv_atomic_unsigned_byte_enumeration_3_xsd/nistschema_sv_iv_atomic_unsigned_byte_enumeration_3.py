from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedByte-enumeration-3-NS"


class NistschemaSvIvAtomicUnsignedByteEnumeration3Type(Enum):
    VALUE_61 = 61
    VALUE_8 = 8
    VALUE_7 = 7
    VALUE_101 = 101
    VALUE_255 = 255
    VALUE_111 = 111
    VALUE_47 = 47
    VALUE_66 = 66
    VALUE_91 = 91
    VALUE_99 = 99


@dataclass(kw_only=True)
class NistschemaSvIvAtomicUnsignedByteEnumeration3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedByte-enumeration-3"
        namespace = "NISTSchema-SV-IV-atomic-unsignedByte-enumeration-3-NS"

    value: NistschemaSvIvAtomicUnsignedByteEnumeration3Type = field()
