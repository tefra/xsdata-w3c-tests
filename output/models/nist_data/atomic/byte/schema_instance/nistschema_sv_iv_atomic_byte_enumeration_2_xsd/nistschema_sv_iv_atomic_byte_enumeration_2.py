from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-byte-enumeration-2-NS"


class NistschemaSvIvAtomicByteEnumeration2Type(Enum):
    VALUE_9 = 9
    VALUE_127 = 127
    VALUE_64 = 64
    VALUE_MINUS_81 = -81
    VALUE_3 = 3
    VALUE_MINUS_7 = -7
    VALUE_MINUS_93 = -93
    VALUE_50 = 50


@dataclass(kw_only=True)
class NistschemaSvIvAtomicByteEnumeration2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-byte-enumeration-2"
        namespace = "NISTSchema-SV-IV-atomic-byte-enumeration-2-NS"

    value: NistschemaSvIvAtomicByteEnumeration2Type = field(
        metadata={
            "required": True,
        }
    )
