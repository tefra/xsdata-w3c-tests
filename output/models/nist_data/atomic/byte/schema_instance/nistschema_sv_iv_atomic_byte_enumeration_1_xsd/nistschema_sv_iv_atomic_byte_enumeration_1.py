from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-byte-enumeration-1-NS"


class NistschemaSvIvAtomicByteEnumeration1Type(Enum):
    """
    :cvar VALUE_MINUS_5:
    :cvar VALUE_MINUS_4:
    :cvar VALUE_MINUS_7:
    :cvar VALUE_88:
    :cvar VALUE_MINUS_128:
    :cvar VALUE_20:
    :cvar VALUE_127:
    :cvar VALUE_MINUS_59:
    :cvar VALUE_84:
    """
    VALUE_MINUS_5 = -5
    VALUE_MINUS_4 = -4
    VALUE_MINUS_7 = -7
    VALUE_88 = 88
    VALUE_MINUS_128 = -128
    VALUE_20 = 20
    VALUE_127 = 127
    VALUE_MINUS_59 = -59
    VALUE_84 = 84


@dataclass
class NistschemaSvIvAtomicByteEnumeration1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-byte-enumeration-1"
        namespace = "NISTSchema-SV-IV-atomic-byte-enumeration-1-NS"

    value: Optional[NistschemaSvIvAtomicByteEnumeration1Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
