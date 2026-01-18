from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedByte-enumeration-2-NS"


class NistschemaSvIvAtomicUnsignedByteEnumeration2Type(Enum):
    VALUE_8 = 8
    VALUE_40 = 40
    VALUE_6 = 6
    VALUE_65 = 65
    VALUE_49 = 49


@dataclass(kw_only=True)
class NistschemaSvIvAtomicUnsignedByteEnumeration2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedByte-enumeration-2"
        namespace = "NISTSchema-SV-IV-atomic-unsignedByte-enumeration-2-NS"

    value: NistschemaSvIvAtomicUnsignedByteEnumeration2Type = field(
        metadata={
            "required": True,
        }
    )
