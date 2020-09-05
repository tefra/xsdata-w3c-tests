from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-dateTime-enumeration-3-NS"


class NistschemaSvIvAtomicDateTimeEnumeration3Type(Enum):
    """
    :cvar VALUE_1978_10_23_T05_45_02:
    :cvar VALUE_1985_02_19_T04_06_18:
    :cvar VALUE_2019_08_14_T05_07_30:
    :cvar VALUE_2030_09_14_T23_19_53:
    :cvar VALUE_2000_08_25_T10_14_42:
    :cvar VALUE_1975_03_11_T11_29_35:
    :cvar VALUE_2019_01_15_T02_01_47:
    :cvar VALUE_1977_04_10_T16_52_34:
    :cvar VALUE_1996_03_21_T14_27_49:
    """
    VALUE_1978_10_23_T05_45_02 = "1978-10-23T05:45:02"
    VALUE_1985_02_19_T04_06_18 = "1985-02-19T04:06:18"
    VALUE_2019_08_14_T05_07_30 = "2019-08-14T05:07:30"
    VALUE_2030_09_14_T23_19_53 = "2030-09-14T23:19:53"
    VALUE_2000_08_25_T10_14_42 = "2000-08-25T10:14:42"
    VALUE_1975_03_11_T11_29_35 = "1975-03-11T11:29:35"
    VALUE_2019_01_15_T02_01_47 = "2019-01-15T02:01:47"
    VALUE_1977_04_10_T16_52_34 = "1977-04-10T16:52:34"
    VALUE_1996_03_21_T14_27_49 = "1996-03-21T14:27:49"


@dataclass
class NistschemaSvIvAtomicDateTimeEnumeration3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-dateTime-enumeration-3"
        namespace = "NISTSchema-SV-IV-atomic-dateTime-enumeration-3-NS"

    value: Optional[NistschemaSvIvAtomicDateTimeEnumeration3Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
