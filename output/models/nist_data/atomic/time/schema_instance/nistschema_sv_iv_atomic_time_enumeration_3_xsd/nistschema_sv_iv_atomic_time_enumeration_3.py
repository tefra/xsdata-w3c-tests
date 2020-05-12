from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-time-enumeration-3-NS"


class NistschemaSvIvAtomicTimeEnumeration3Type(Enum):
    """
    :cvar VALUE_03_47_11:
    :cvar VALUE_16_04_46:
    :cvar VALUE_01_35_26:
    :cvar VALUE_22_39_51:
    :cvar VALUE_15_13_10:
    :cvar VALUE_23_32_59:
    :cvar VALUE_02_39_19:
    """
    VALUE_03_47_11 = "03:47:11"
    VALUE_16_04_46 = "16:04:46"
    VALUE_01_35_26 = "01:35:26"
    VALUE_22_39_51 = "22:39:51"
    VALUE_15_13_10 = "15:13:10"
    VALUE_23_32_59 = "23:32:59"
    VALUE_02_39_19 = "02:39:19"


@dataclass
class NistschemaSvIvAtomicTimeEnumeration3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-time-enumeration-3"
        namespace = "NISTSchema-SV-IV-atomic-time-enumeration-3-NS"

    value: Optional[NistschemaSvIvAtomicTimeEnumeration3Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
