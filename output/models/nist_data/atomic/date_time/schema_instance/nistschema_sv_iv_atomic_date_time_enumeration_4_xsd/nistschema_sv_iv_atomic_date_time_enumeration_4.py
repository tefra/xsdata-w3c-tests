from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-dateTime-enumeration-4-NS"


class NistschemaSvIvAtomicDateTimeEnumeration4Type(Enum):
    """
    :cvar VALUE_1975_03_26_T02_01_19:
    :cvar VALUE_1989_06_12_T23_17_57:
    :cvar VALUE_1990_10_27_T15_40_41:
    :cvar VALUE_1999_01_22_T23_05_35:
    :cvar VALUE_2000_08_27_T05_34_53:
    :cvar VALUE_2011_02_13_T13_12_56:
    :cvar VALUE_2018_02_02_T20_25_48:
    :cvar VALUE_2019_11_24_T15_12_13:
    """
    VALUE_1975_03_26_T02_01_19 = "1975-03-26T02:01:19"
    VALUE_1989_06_12_T23_17_57 = "1989-06-12T23:17:57"
    VALUE_1990_10_27_T15_40_41 = "1990-10-27T15:40:41"
    VALUE_1999_01_22_T23_05_35 = "1999-01-22T23:05:35"
    VALUE_2000_08_27_T05_34_53 = "2000-08-27T05:34:53"
    VALUE_2011_02_13_T13_12_56 = "2011-02-13T13:12:56"
    VALUE_2018_02_02_T20_25_48 = "2018-02-02T20:25:48"
    VALUE_2019_11_24_T15_12_13 = "2019-11-24T15:12:13"


@dataclass
class NistschemaSvIvAtomicDateTimeEnumeration4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-dateTime-enumeration-4"
        namespace = "NISTSchema-SV-IV-atomic-dateTime-enumeration-4-NS"

    value: Optional[NistschemaSvIvAtomicDateTimeEnumeration4Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
