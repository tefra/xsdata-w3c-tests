from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedByte-enumeration-3-NS"


class NistschemaSvIvAtomicUnsignedByteEnumeration3Type(Enum):
    """
    :cvar VALUE_61:
    :cvar VALUE_8:
    :cvar VALUE_7:
    :cvar VALUE_101:
    :cvar VALUE_255:
    :cvar VALUE_111:
    :cvar VALUE_47:
    :cvar VALUE_66:
    :cvar VALUE_91:
    :cvar VALUE_99:
    """
    VALUE_61 = 61
    VALUE_8 = 8
    VALUE_7 = 7
    VALUE_101 = 101
    VALUE_255 = 255
    VALUE_111 = 111
    VALUE_47 = 47
    VALUE_66 = 66
    VALUE_91 = 91
    VALUE_99 = 99


@dataclass
class NistschemaSvIvAtomicUnsignedByteEnumeration3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedByte-enumeration-3"
        namespace = "NISTSchema-SV-IV-atomic-unsignedByte-enumeration-3-NS"

    value: Optional[NistschemaSvIvAtomicUnsignedByteEnumeration3Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
