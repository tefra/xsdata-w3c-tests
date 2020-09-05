from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gMonthDay-enumeration-3-NS"


class NistschemaSvIvAtomicGMonthDayEnumeration3Type(Enum):
    """
    :cvar VALUE_12_23:
    :cvar VALUE_07_11:
    :cvar VALUE_06_24:
    :cvar VALUE_10_27:
    :cvar VALUE_09_07:
    :cvar VALUE_03_29:
    :cvar VALUE_12_01:
    :cvar VALUE_01_29:
    :cvar VALUE_07_09:
    :cvar VALUE_10_05:
    """
    VALUE_12_23 = "--12-23"
    VALUE_07_11 = "--07-11"
    VALUE_06_24 = "--06-24"
    VALUE_10_27 = "--10-27"
    VALUE_09_07 = "--09-07"
    VALUE_03_29 = "--03-29"
    VALUE_12_01 = "--12-01"
    VALUE_01_29 = "--01-29"
    VALUE_07_09 = "--07-09"
    VALUE_10_05 = "--10-05"


@dataclass
class NistschemaSvIvAtomicGMonthDayEnumeration3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gMonthDay-enumeration-3"
        namespace = "NISTSchema-SV-IV-atomic-gMonthDay-enumeration-3-NS"

    value: Optional[NistschemaSvIvAtomicGMonthDayEnumeration3Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
