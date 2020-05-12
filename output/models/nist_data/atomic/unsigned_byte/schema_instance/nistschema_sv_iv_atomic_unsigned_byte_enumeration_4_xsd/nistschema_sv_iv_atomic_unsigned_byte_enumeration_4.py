from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedByte-enumeration-4-NS"


class NistschemaSvIvAtomicUnsignedByteEnumeration4Type(Enum):
    """
    :cvar VALUE_8:
    :cvar VALUE_43:
    :cvar VALUE_15:
    :cvar VALUE_255:
    :cvar VALUE_83:
    :cvar VALUE_72:
    :cvar VALUE_71:
    """
    VALUE_8 = 8
    VALUE_43 = 43
    VALUE_15 = 15
    VALUE_255 = 255
    VALUE_83 = 83
    VALUE_72 = 72
    VALUE_71 = 71


@dataclass
class NistschemaSvIvAtomicUnsignedByteEnumeration4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedByte-enumeration-4"
        namespace = "NISTSchema-SV-IV-atomic-unsignedByte-enumeration-4-NS"

    value: Optional[NistschemaSvIvAtomicUnsignedByteEnumeration4Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
