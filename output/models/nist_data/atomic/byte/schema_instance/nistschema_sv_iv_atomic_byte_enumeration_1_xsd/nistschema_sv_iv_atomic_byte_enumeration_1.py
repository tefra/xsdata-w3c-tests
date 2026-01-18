from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-byte-enumeration-1-NS"


class NistschemaSvIvAtomicByteEnumeration1Type(Enum):
    VALUE_MINUS_5 = -5
    VALUE_MINUS_4 = -4
    VALUE_MINUS_7 = -7
    VALUE_88 = 88
    VALUE_MINUS_128 = -128
    VALUE_20 = 20
    VALUE_127 = 127
    VALUE_MINUS_59 = -59
    VALUE_84 = 84


@dataclass(kw_only=True)
class NistschemaSvIvAtomicByteEnumeration1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-byte-enumeration-1"
        namespace = "NISTSchema-SV-IV-atomic-byte-enumeration-1-NS"

    value: NistschemaSvIvAtomicByteEnumeration1Type = field(
        metadata={
            "required": True,
        }
    )
