from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedByte-enumeration-1-NS"


class NistschemaSvIvAtomicUnsignedByteEnumeration1Type(Enum):
    """
    :cvar VALUE_21:
    :cvar VALUE_255:
    :cvar VALUE_57:
    :cvar VALUE_70:
    :cvar VALUE_6:
    :cvar VALUE_45:
    :cvar VALUE_8:
    :cvar VALUE_90:
    :cvar VALUE_85:
    :cvar VALUE_14:
    """
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


@dataclass
class NistschemaSvIvAtomicUnsignedByteEnumeration1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedByte-enumeration-1"
        namespace = "NISTSchema-SV-IV-atomic-unsignedByte-enumeration-1-NS"

    value: Optional[NistschemaSvIvAtomicUnsignedByteEnumeration1Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
