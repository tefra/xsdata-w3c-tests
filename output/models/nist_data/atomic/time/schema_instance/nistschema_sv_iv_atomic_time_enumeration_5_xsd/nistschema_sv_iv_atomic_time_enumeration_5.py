from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-time-enumeration-5-NS"


class NistschemaSvIvAtomicTimeEnumeration5Type(Enum):
    """
    :cvar VALUE_06_18_04:
    :cvar VALUE_07_45_10:
    :cvar VALUE_12_06_46:
    :cvar VALUE_21_01_58:
    :cvar VALUE_05_34_33:
    :cvar VALUE_22_22_06:
    :cvar VALUE_12_17_04:
    """
    VALUE_06_18_04 = "06:18:04"
    VALUE_07_45_10 = "07:45:10"
    VALUE_12_06_46 = "12:06:46"
    VALUE_21_01_58 = "21:01:58"
    VALUE_05_34_33 = "05:34:33"
    VALUE_22_22_06 = "22:22:06"
    VALUE_12_17_04 = "12:17:04"


@dataclass
class NistschemaSvIvAtomicTimeEnumeration5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-time-enumeration-5"
        namespace = "NISTSchema-SV-IV-atomic-time-enumeration-5-NS"

    value: Optional[NistschemaSvIvAtomicTimeEnumeration5Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
