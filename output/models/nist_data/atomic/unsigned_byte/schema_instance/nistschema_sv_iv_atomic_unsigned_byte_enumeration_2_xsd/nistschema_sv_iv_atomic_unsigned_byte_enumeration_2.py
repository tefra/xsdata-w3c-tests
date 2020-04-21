from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedByte-enumeration-2-NS"


class NistschemaSvIvAtomicUnsignedByteEnumeration2Type(Enum):
    """
    :cvar VALUE_40:
    :cvar VALUE_49:
    :cvar VALUE_6:
    :cvar VALUE_65:
    :cvar VALUE_8:
    """
    VALUE_40 = 40
    VALUE_49 = 49
    VALUE_6 = 6
    VALUE_65 = 65
    VALUE_8 = 8


@dataclass
class NistschemaSvIvAtomicUnsignedByteEnumeration2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedByte-enumeration-2"
        namespace = "NISTSchema-SV-IV-atomic-unsignedByte-enumeration-2-NS"

    value: Optional[NistschemaSvIvAtomicUnsignedByteEnumeration2Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
