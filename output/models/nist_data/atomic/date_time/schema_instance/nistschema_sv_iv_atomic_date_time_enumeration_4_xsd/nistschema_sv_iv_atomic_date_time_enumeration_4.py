from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-dateTime-enumeration-4-NS"


class NistschemaSvIvAtomicDateTimeEnumeration4Type(Enum):
    VALUE_2000_08_27_T05_34_53 = XmlDateTime(2000, 8, 27, 5, 34, 53)
    VALUE_1999_01_22_T23_05_35 = XmlDateTime(1999, 1, 22, 23, 5, 35)
    VALUE_2018_02_02_T20_25_48 = XmlDateTime(2018, 2, 2, 20, 25, 48)
    VALUE_1990_10_27_T15_40_41 = XmlDateTime(1990, 10, 27, 15, 40, 41)
    VALUE_1989_06_12_T23_17_57 = XmlDateTime(1989, 6, 12, 23, 17, 57)
    VALUE_2019_11_24_T15_12_13 = XmlDateTime(2019, 11, 24, 15, 12, 13)
    VALUE_2011_02_13_T13_12_56 = XmlDateTime(2011, 2, 13, 13, 12, 56)
    VALUE_1975_03_26_T02_01_19 = XmlDateTime(1975, 3, 26, 2, 1, 19)


@dataclass
class NistschemaSvIvAtomicDateTimeEnumeration4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-dateTime-enumeration-4"
        namespace = "NISTSchema-SV-IV-atomic-dateTime-enumeration-4-NS"

    value: Optional[NistschemaSvIvAtomicDateTimeEnumeration4Type] = field(
        default=None
    )
