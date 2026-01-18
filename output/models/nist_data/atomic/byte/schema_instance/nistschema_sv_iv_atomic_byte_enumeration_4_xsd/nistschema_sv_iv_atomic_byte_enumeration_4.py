from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-byte-enumeration-4-NS"


class NistschemaSvIvAtomicByteEnumeration4Type(Enum):
    VALUE_MINUS_5 = -5
    VALUE_96 = 96
    VALUE_127 = 127
    VALUE_MINUS_48 = -48
    VALUE_33 = 33
    VALUE_69 = 69
    VALUE_MINUS_60 = -60
    VALUE_MINUS_86 = -86


@dataclass(kw_only=True)
class NistschemaSvIvAtomicByteEnumeration4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-byte-enumeration-4"
        namespace = "NISTSchema-SV-IV-atomic-byte-enumeration-4-NS"

    value: NistschemaSvIvAtomicByteEnumeration4Type = field(
        metadata={
            "required": True,
        }
    )
