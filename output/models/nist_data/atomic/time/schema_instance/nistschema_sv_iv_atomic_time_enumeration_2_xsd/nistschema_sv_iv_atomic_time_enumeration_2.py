from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-time-enumeration-2-NS"


class NistschemaSvIvAtomicTimeEnumeration2Type(Enum):
    """
    :cvar VALUE_02_02_10:
    :cvar VALUE_06_00_33:
    :cvar VALUE_10_32_33:
    :cvar VALUE_11_14_02:
    :cvar VALUE_11_18_46:
    :cvar VALUE_14_01_48:
    """
    VALUE_02_02_10 = "02:02:10"
    VALUE_06_00_33 = "06:00:33"
    VALUE_10_32_33 = "10:32:33"
    VALUE_11_14_02 = "11:14:02"
    VALUE_11_18_46 = "11:18:46"
    VALUE_14_01_48 = "14:01:48"


@dataclass
class NistschemaSvIvAtomicTimeEnumeration2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-time-enumeration-2"
        namespace = "NISTSchema-SV-IV-atomic-time-enumeration-2-NS"

    value: Optional[NistschemaSvIvAtomicTimeEnumeration2Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )