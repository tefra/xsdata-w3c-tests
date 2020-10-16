from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-time-enumeration-4-NS"


class NistschemaSvIvAtomicTimeEnumeration4Type(Enum):
    """
    :cvar VALUE_18_04_07:
    :cvar VALUE_05_41_14:
    :cvar VALUE_15_07_15:
    :cvar VALUE_01_18_17:
    :cvar VALUE_01_13_21:
    :cvar VALUE_23_24_35:
    :cvar VALUE_15_25_08:
    :cvar VALUE_18_20_35:
    :cvar VALUE_03_53_17:
    """
    VALUE_18_04_07 = "18:04:07"
    VALUE_05_41_14 = "05:41:14"
    VALUE_15_07_15 = "15:07:15"
    VALUE_01_18_17 = "01:18:17"
    VALUE_01_13_21 = "01:13:21"
    VALUE_23_24_35 = "23:24:35"
    VALUE_15_25_08 = "15:25:08"
    VALUE_18_20_35 = "18:20:35"
    VALUE_03_53_17 = "03:53:17"


@dataclass
class NistschemaSvIvAtomicTimeEnumeration4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-time-enumeration-4"
        namespace = "NISTSchema-SV-IV-atomic-time-enumeration-4-NS"

    value: Optional[NistschemaSvIvAtomicTimeEnumeration4Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
