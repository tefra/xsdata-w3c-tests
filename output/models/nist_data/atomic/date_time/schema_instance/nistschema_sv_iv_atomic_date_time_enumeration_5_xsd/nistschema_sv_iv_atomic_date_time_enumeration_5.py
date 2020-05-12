from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-dateTime-enumeration-5-NS"


class NistschemaSvIvAtomicDateTimeEnumeration5Type(Enum):
    """
    :cvar VALUE_1990_01_04_T22_40_05:
    :cvar VALUE_2011_07_27_T05_09_10:
    :cvar VALUE_1996_12_01_T14_47_04:
    :cvar VALUE_1998_08_05_T19_34_41:
    :cvar VALUE_1989_04_17_T09_42_01:
    :cvar VALUE_1980_08_05_T22_54_49:
    """
    VALUE_1990_01_04_T22_40_05 = "1990-01-04T22:40:05"
    VALUE_2011_07_27_T05_09_10 = "2011-07-27T05:09:10"
    VALUE_1996_12_01_T14_47_04 = "1996-12-01T14:47:04"
    VALUE_1998_08_05_T19_34_41 = "1998-08-05T19:34:41"
    VALUE_1989_04_17_T09_42_01 = "1989-04-17T09:42:01"
    VALUE_1980_08_05_T22_54_49 = "1980-08-05T22:54:49"


@dataclass
class NistschemaSvIvAtomicDateTimeEnumeration5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-dateTime-enumeration-5"
        namespace = "NISTSchema-SV-IV-atomic-dateTime-enumeration-5-NS"

    value: Optional[NistschemaSvIvAtomicDateTimeEnumeration5Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
