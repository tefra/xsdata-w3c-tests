from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedByte-enumeration-2-NS"


class NistschemaSvIvAtomicUnsignedByteEnumeration2Type(Enum):
    VALUE_8 = 8
    VALUE_40 = 40
    VALUE_6 = 6
    VALUE_65 = 65
    VALUE_49 = 49


@dataclass
class NistschemaSvIvAtomicUnsignedByteEnumeration2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedByte-enumeration-2"
        namespace = "NISTSchema-SV-IV-atomic-unsignedByte-enumeration-2-NS"

    value: Optional[NistschemaSvIvAtomicUnsignedByteEnumeration2Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
