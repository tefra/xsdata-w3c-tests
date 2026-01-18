from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedByte-enumeration-1-NS"


class NistschemaSvIvAtomicUnsignedByteEnumeration1Type(Enum):
    VALUE_21 = 21
    VALUE_255 = 255
    VALUE_57 = 57
    VALUE_70 = 70
    VALUE_6 = 6
    VALUE_45 = 45
    VALUE_8 = 8
    VALUE_90 = 90
    VALUE_85 = 85
    VALUE_14 = 14


@dataclass(kw_only=True)
class NistschemaSvIvAtomicUnsignedByteEnumeration1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedByte-enumeration-1"
        namespace = "NISTSchema-SV-IV-atomic-unsignedByte-enumeration-1-NS"

    value: NistschemaSvIvAtomicUnsignedByteEnumeration1Type = field(
        metadata={
            "required": True,
        }
    )
