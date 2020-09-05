from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-byte-enumeration-4-NS"


class NistschemaSvIvAtomicByteEnumeration4Type(Enum):
    """
    :cvar VALUE_MINUS_5:
    :cvar VALUE_96:
    :cvar VALUE_127:
    :cvar VALUE_MINUS_48:
    :cvar VALUE_33:
    :cvar VALUE_69:
    :cvar VALUE_MINUS_60:
    :cvar VALUE_MINUS_86:
    """
    VALUE_MINUS_5 = -5
    VALUE_96 = 96
    VALUE_127 = 127
    VALUE_MINUS_48 = -48
    VALUE_33 = 33
    VALUE_69 = 69
    VALUE_MINUS_60 = -60
    VALUE_MINUS_86 = -86


@dataclass
class NistschemaSvIvAtomicByteEnumeration4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-byte-enumeration-4"
        namespace = "NISTSchema-SV-IV-atomic-byte-enumeration-4-NS"

    value: Optional[NistschemaSvIvAtomicByteEnumeration4Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
