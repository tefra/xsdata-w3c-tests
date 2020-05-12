from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gMonthDay-enumeration-4-NS"


class NistschemaSvIvAtomicGMonthDayEnumeration4Type(Enum):
    """
    :cvar VALUE_06_07:
    :cvar VALUE_11_20:
    :cvar VALUE_01_29:
    :cvar VALUE_11_11:
    :cvar VALUE_11_17:
    :cvar VALUE_05_08:
    :cvar VALUE_07_06:
    :cvar VALUE_12_01:
    :cvar VALUE_05_07:
    :cvar VALUE_09_03:
    """
    VALUE_06_07 = "--06-07"
    VALUE_11_20 = "--11-20"
    VALUE_01_29 = "--01-29"
    VALUE_11_11 = "--11-11"
    VALUE_11_17 = "--11-17"
    VALUE_05_08 = "--05-08"
    VALUE_07_06 = "--07-06"
    VALUE_12_01 = "--12-01"
    VALUE_05_07 = "--05-07"
    VALUE_09_03 = "--09-03"


@dataclass
class NistschemaSvIvAtomicGMonthDayEnumeration4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gMonthDay-enumeration-4"
        namespace = "NISTSchema-SV-IV-atomic-gMonthDay-enumeration-4-NS"

    value: Optional[NistschemaSvIvAtomicGMonthDayEnumeration4Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
