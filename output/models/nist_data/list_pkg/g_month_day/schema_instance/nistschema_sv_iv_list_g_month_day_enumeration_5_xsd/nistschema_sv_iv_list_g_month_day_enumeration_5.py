from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-list-gMonthDay-enumeration-5-NS"


class NistschemaSvIvListGMonthDayEnumeration5Type(Enum):
    VALUE_08_12_06_25_07_14_05_27_07_26_12_22_09_25_08_28_09_05_02_23 = (
            XmlPeriod("--08-12"),
            XmlPeriod("--06-25"),
            XmlPeriod("--07-14"),
            XmlPeriod("--05-27"),
            XmlPeriod("--07-26"),
            XmlPeriod("--12-22"),
            XmlPeriod("--09-25"),
            XmlPeriod("--08-28"),
            XmlPeriod("--09-05"),
            XmlPeriod("--02-23"),
        )
    VALUE_02_11_10_02_09_27_03_02_08_31_03_16_11_07_03_29_09_16 = (
            XmlPeriod("--02-11"),
            XmlPeriod("--10-02"),
            XmlPeriod("--09-27"),
            XmlPeriod("--03-02"),
            XmlPeriod("--08-31"),
            XmlPeriod("--03-16"),
            XmlPeriod("--11-07"),
            XmlPeriod("--03-29"),
            XmlPeriod("--09-16"),
        )
    VALUE_10_13_09_15_01_10_02_24_01_27_08_10_11_23 = (
            XmlPeriod("--10-13"),
            XmlPeriod("--09-15"),
            XmlPeriod("--01-10"),
            XmlPeriod("--02-24"),
            XmlPeriod("--01-27"),
            XmlPeriod("--08-10"),
            XmlPeriod("--11-23"),
        )
    VALUE_01_26_10_22_10_19_04_02_01_16_01_26_05_10_12_05 = (
            XmlPeriod("--01-26"),
            XmlPeriod("--10-22"),
            XmlPeriod("--10-19"),
            XmlPeriod("--04-02"),
            XmlPeriod("--01-16"),
            XmlPeriod("--01-26"),
            XmlPeriod("--05-10"),
            XmlPeriod("--12-05"),
        )
    VALUE_09_25_08_01_01_26_06_24_03_21_02_10_06_26_06_06_03_28 = (
            XmlPeriod("--09-25"),
            XmlPeriod("--08-01"),
            XmlPeriod("--01-26"),
            XmlPeriod("--06-24"),
            XmlPeriod("--03-21"),
            XmlPeriod("--02-10"),
            XmlPeriod("--06-26"),
            XmlPeriod("--06-06"),
            XmlPeriod("--03-28"),
        )
    VALUE_10_05_07_14_10_13_07_11_06_05_12_19_07_02_12_30_07_05 = (
            XmlPeriod("--10-05"),
            XmlPeriod("--07-14"),
            XmlPeriod("--10-13"),
            XmlPeriod("--07-11"),
            XmlPeriod("--06-05"),
            XmlPeriod("--12-19"),
            XmlPeriod("--07-02"),
            XmlPeriod("--12-30"),
            XmlPeriod("--07-05"),
        )
    VALUE_12_06_06_20_06_24_10_01_07_20 = (
            XmlPeriod("--12-06"),
            XmlPeriod("--06-20"),
            XmlPeriod("--06-24"),
            XmlPeriod("--10-01"),
            XmlPeriod("--07-20"),
        )


@dataclass
class NistschemaSvIvListGMonthDayEnumeration5:
    class Meta:
        name = "NISTSchema-SV-IV-list-gMonthDay-enumeration-5"
        namespace = "NISTSchema-SV-IV-list-gMonthDay-enumeration-5-NS"

    value: Optional[NistschemaSvIvListGMonthDayEnumeration5Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
