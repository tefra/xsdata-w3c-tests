from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-dateTime-enumeration-3-NS"


class NistschemaSvIvAtomicDateTimeEnumeration3Type(Enum):
    VALUE_1978_10_23_T05_45_02 = XmlDateTime(1978, 10, 23, 5, 45, 2)
    VALUE_1985_02_19_T04_06_18 = XmlDateTime(1985, 2, 19, 4, 6, 18)
    VALUE_2019_08_14_T05_07_30 = XmlDateTime(2019, 8, 14, 5, 7, 30)
    VALUE_2030_09_14_T23_19_53 = XmlDateTime(2030, 9, 14, 23, 19, 53)
    VALUE_2000_08_25_T10_14_42 = XmlDateTime(2000, 8, 25, 10, 14, 42)
    VALUE_1975_03_11_T11_29_35 = XmlDateTime(1975, 3, 11, 11, 29, 35)
    VALUE_2019_01_15_T02_01_47 = XmlDateTime(2019, 1, 15, 2, 1, 47)
    VALUE_1977_04_10_T16_52_34 = XmlDateTime(1977, 4, 10, 16, 52, 34)
    VALUE_1996_03_21_T14_27_49 = XmlDateTime(1996, 3, 21, 14, 27, 49)


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDateTimeEnumeration3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-dateTime-enumeration-3"
        namespace = "NISTSchema-SV-IV-atomic-dateTime-enumeration-3-NS"

    value: NistschemaSvIvAtomicDateTimeEnumeration3Type = field()
