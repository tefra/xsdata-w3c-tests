from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-dateTime-enumeration-5-NS"


class NistschemaSvIvAtomicDateTimeEnumeration5Type(Enum):
    VALUE_1990_01_04_T22_40_05 = XmlDateTime(1990, 1, 4, 22, 40, 5)
    VALUE_2011_07_27_T05_09_10 = XmlDateTime(2011, 7, 27, 5, 9, 10)
    VALUE_1996_12_01_T14_47_04 = XmlDateTime(1996, 12, 1, 14, 47, 4)
    VALUE_1998_08_05_T19_34_41 = XmlDateTime(1998, 8, 5, 19, 34, 41)
    VALUE_1989_04_17_T09_42_01 = XmlDateTime(1989, 4, 17, 9, 42, 1)
    VALUE_1980_08_05_T22_54_49 = XmlDateTime(1980, 8, 5, 22, 54, 49)


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDateTimeEnumeration5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-dateTime-enumeration-5"
        namespace = "NISTSchema-SV-IV-atomic-dateTime-enumeration-5-NS"

    value: NistschemaSvIvAtomicDateTimeEnumeration5Type = field()
