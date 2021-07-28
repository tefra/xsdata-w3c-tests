from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-list-gMonthDay-enumeration-3-NS"


class NistschemaSvIvListGMonthDayEnumeration3Type(Enum):
    VALUE_10_27_08_13_07_15_02_01_01_16_06_17_10_05_01_21 = (
            XmlPeriod("--10-27"),
            XmlPeriod("--08-13"),
            XmlPeriod("--07-15"),
            XmlPeriod("--02-01"),
            XmlPeriod("--01-16"),
            XmlPeriod("--06-17"),
            XmlPeriod("--10-05"),
            XmlPeriod("--01-21"),
        )
    VALUE_11_15_12_29_10_05_05_21_03_08_05_29 = (
            XmlPeriod("--11-15"),
            XmlPeriod("--12-29"),
            XmlPeriod("--10-05"),
            XmlPeriod("--05-21"),
            XmlPeriod("--03-08"),
            XmlPeriod("--05-29"),
        )
    VALUE_06_29_01_23_07_14_09_22_02_24_01_05 = (
            XmlPeriod("--06-29"),
            XmlPeriod("--01-23"),
            XmlPeriod("--07-14"),
            XmlPeriod("--09-22"),
            XmlPeriod("--02-24"),
            XmlPeriod("--01-05"),
        )
    VALUE_04_08_03_18_05_15_08_27_04_28_01_27_11_13_08_28 = (
            XmlPeriod("--04-08"),
            XmlPeriod("--03-18"),
            XmlPeriod("--05-15"),
            XmlPeriod("--08-27"),
            XmlPeriod("--04-28"),
            XmlPeriod("--01-27"),
            XmlPeriod("--11-13"),
            XmlPeriod("--08-28"),
        )
    VALUE_09_13_06_20_03_06_09_19_04_02_11_23 = (
            XmlPeriod("--09-13"),
            XmlPeriod("--06-20"),
            XmlPeriod("--03-06"),
            XmlPeriod("--09-19"),
            XmlPeriod("--04-02"),
            XmlPeriod("--11-23"),
        )
    VALUE_06_11_11_05_08_18_09_11_05_29_08_21_09_10_10_14 = (
            XmlPeriod("--06-11"),
            XmlPeriod("--11-05"),
            XmlPeriod("--08-18"),
            XmlPeriod("--09-11"),
            XmlPeriod("--05-29"),
            XmlPeriod("--08-21"),
            XmlPeriod("--09-10"),
            XmlPeriod("--10-14"),
        )


@dataclass
class NistschemaSvIvListGMonthDayEnumeration3:
    class Meta:
        name = "NISTSchema-SV-IV-list-gMonthDay-enumeration-3"
        namespace = "NISTSchema-SV-IV-list-gMonthDay-enumeration-3-NS"

    value: Optional[NistschemaSvIvListGMonthDayEnumeration3Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
