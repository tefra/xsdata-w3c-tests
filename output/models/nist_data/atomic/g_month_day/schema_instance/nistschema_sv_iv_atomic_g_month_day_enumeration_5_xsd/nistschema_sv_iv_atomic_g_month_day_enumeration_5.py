from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gMonthDay-enumeration-5-NS"


class NistschemaSvIvAtomicGMonthDayEnumeration5Type(Enum):
    """
    :cvar VALUE_02_23:
    :cvar VALUE_03_28:
    :cvar VALUE_04_03:
    :cvar VALUE_05_21:
    :cvar VALUE_07_11:
    :cvar VALUE_08_07:
    :cvar VALUE_09_03:
    :cvar VALUE_09_13:
    :cvar VALUE_09_18:
    """
    VALUE_02_23 = "--02-23"
    VALUE_03_28 = "--03-28"
    VALUE_04_03 = "--04-03"
    VALUE_05_21 = "--05-21"
    VALUE_07_11 = "--07-11"
    VALUE_08_07 = "--08-07"
    VALUE_09_03 = "--09-03"
    VALUE_09_13 = "--09-13"
    VALUE_09_18 = "--09-18"


@dataclass
class NistschemaSvIvAtomicGMonthDayEnumeration5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gMonthDay-enumeration-5"
        namespace = "NISTSchema-SV-IV-atomic-gMonthDay-enumeration-5-NS"

    value: Optional[NistschemaSvIvAtomicGMonthDayEnumeration5Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
