from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedByte-enumeration-5-NS"


class NistschemaSvIvAtomicUnsignedByteEnumeration5Type(Enum):
    VALUE_1 = 1
    VALUE_21 = 21
    VALUE_55 = 55
    VALUE_9 = 9
    VALUE_132 = 132
    VALUE_255 = 255
    VALUE_17 = 17


@dataclass(kw_only=True)
class NistschemaSvIvAtomicUnsignedByteEnumeration5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedByte-enumeration-5"
        namespace = "NISTSchema-SV-IV-atomic-unsignedByte-enumeration-5-NS"

    value: NistschemaSvIvAtomicUnsignedByteEnumeration5Type = field()
