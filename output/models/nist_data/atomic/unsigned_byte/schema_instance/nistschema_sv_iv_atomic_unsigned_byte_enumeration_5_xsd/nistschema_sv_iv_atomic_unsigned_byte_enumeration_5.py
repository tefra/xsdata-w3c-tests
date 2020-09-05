from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedByte-enumeration-5-NS"


class NistschemaSvIvAtomicUnsignedByteEnumeration5Type(Enum):
    """
    :cvar VALUE_1:
    :cvar VALUE_21:
    :cvar VALUE_55:
    :cvar VALUE_9:
    :cvar VALUE_132:
    :cvar VALUE_255:
    :cvar VALUE_17:
    """
    VALUE_1 = 1
    VALUE_21 = 21
    VALUE_55 = 55
    VALUE_9 = 9
    VALUE_132 = 132
    VALUE_255 = 255
    VALUE_17 = 17


@dataclass
class NistschemaSvIvAtomicUnsignedByteEnumeration5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedByte-enumeration-5"
        namespace = "NISTSchema-SV-IV-atomic-unsignedByte-enumeration-5-NS"

    value: Optional[NistschemaSvIvAtomicUnsignedByteEnumeration5Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
