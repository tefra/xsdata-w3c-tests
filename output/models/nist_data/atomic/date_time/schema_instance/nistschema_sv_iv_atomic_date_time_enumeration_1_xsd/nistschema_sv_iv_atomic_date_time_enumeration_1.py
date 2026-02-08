from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-dateTime-enumeration-1-NS"


class NistschemaSvIvAtomicDateTimeEnumeration1Type(Enum):
    VALUE_2010_02_12_T03_22_00 = XmlDateTime(2010, 2, 12, 3, 22, 0)
    VALUE_1972_11_27_T20_41_04 = XmlDateTime(1972, 11, 27, 20, 41, 4)
    VALUE_2015_08_04_T06_44_16 = XmlDateTime(2015, 8, 4, 6, 44, 16)
    VALUE_2011_05_07_T03_49_38 = XmlDateTime(2011, 5, 7, 3, 49, 38)
    VALUE_2029_12_13_T21_03_46 = XmlDateTime(2029, 12, 13, 21, 3, 46)
    VALUE_2029_04_19_T14_21_30 = XmlDateTime(2029, 4, 19, 14, 21, 30)


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDateTimeEnumeration1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-dateTime-enumeration-1"
        namespace = "NISTSchema-SV-IV-atomic-dateTime-enumeration-1-NS"

    value: NistschemaSvIvAtomicDateTimeEnumeration1Type = field()
