from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-byte-enumeration-5-NS"


class NistschemaSvIvAtomicByteEnumeration5Type(Enum):
    """
    :cvar VALUE_MINUS_128:
    :cvar VALUE_MINUS_3:
    :cvar VALUE_MINUS_35:
    :cvar VALUE_MINUS_45:
    :cvar VALUE_MINUS_5:
    :cvar VALUE_MINUS_89:
    :cvar VALUE_127:
    :cvar VALUE_14:
    :cvar VALUE_41:
    """
    VALUE_MINUS_128 = -128
    VALUE_MINUS_3 = -3
    VALUE_MINUS_35 = -35
    VALUE_MINUS_45 = -45
    VALUE_MINUS_5 = -5
    VALUE_MINUS_89 = -89
    VALUE_127 = 127
    VALUE_14 = 14
    VALUE_41 = 41


@dataclass
class NistschemaSvIvAtomicByteEnumeration5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-byte-enumeration-5"
        namespace = "NISTSchema-SV-IV-atomic-byte-enumeration-5-NS"

    value: Optional[NistschemaSvIvAtomicByteEnumeration5Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
