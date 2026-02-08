from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedByte-enumeration-4-NS"


class NistschemaSvIvAtomicUnsignedByteEnumeration4Type(Enum):
    VALUE_8 = 8
    VALUE_43 = 43
    VALUE_15 = 15
    VALUE_255 = 255
    VALUE_83 = 83
    VALUE_72 = 72
    VALUE_71 = 71


@dataclass(kw_only=True)
class NistschemaSvIvAtomicUnsignedByteEnumeration4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedByte-enumeration-4"
        namespace = "NISTSchema-SV-IV-atomic-unsignedByte-enumeration-4-NS"

    value: NistschemaSvIvAtomicUnsignedByteEnumeration4Type = field()
