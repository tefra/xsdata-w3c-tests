from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

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


@dataclass
class NistschemaSvIvAtomicByteEnumeration3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-byte-enumeration-3"
        namespace = "NISTSchema-SV-IV-atomic-byte-enumeration-3-NS"

    value: Optional[NistschemaSvIvAtomicByteEnumeration3Type] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
