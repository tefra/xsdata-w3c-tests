from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-list-gMonthDay-enumeration-1-NS"


class NistschemaSvIvListGMonthDayEnumeration1Type(Enum):
    VALUE_06_15_07_19_03_23_06_10_12_07_06_12_08_06_09_17_11_15 = (
        XmlPeriod("--06-15"),
        XmlPeriod("--07-19"),
        XmlPeriod("--03-23"),
        XmlPeriod("--06-10"),
        XmlPeriod("--12-07"),
        XmlPeriod("--06-12"),
        XmlPeriod("--08-06"),
        XmlPeriod("--09-17"),
        XmlPeriod("--11-15"),
    )
    VALUE_12_07_05_06_01_17_07_12_06_06_01_14_06_01 = (
        XmlPeriod("--12-07"),
        XmlPeriod("--05-06"),
        XmlPeriod("--01-17"),
        XmlPeriod("--07-12"),
        XmlPeriod("--06-06"),
        XmlPeriod("--01-14"),
        XmlPeriod("--06-01"),
    )
    VALUE_02_09_06_03_07_04_12_24_04_02_03_30_09_13_09_09_07_10 = (
        XmlPeriod("--02-09"),
        XmlPeriod("--06-03"),
        XmlPeriod("--07-04"),
        XmlPeriod("--12-24"),
        XmlPeriod("--04-02"),
        XmlPeriod("--03-30"),
        XmlPeriod("--09-13"),
        XmlPeriod("--09-09"),
        XmlPeriod("--07-10"),
    )
    VALUE_10_18_07_17_11_11_11_02_06_17_02_05 = (
        XmlPeriod("--10-18"),
        XmlPeriod("--07-17"),
        XmlPeriod("--11-11"),
        XmlPeriod("--11-02"),
        XmlPeriod("--06-17"),
        XmlPeriod("--02-05"),
    )
    VALUE_07_14_04_06_01_18_10_07_06_24_03_18_08_20_10_15_07_13 = (
        XmlPeriod("--07-14"),
        XmlPeriod("--04-06"),
        XmlPeriod("--01-18"),
        XmlPeriod("--10-07"),
        XmlPeriod("--06-24"),
        XmlPeriod("--03-18"),
        XmlPeriod("--08-20"),
        XmlPeriod("--10-15"),
        XmlPeriod("--07-13"),
    )
    VALUE_01_07_08_03_01_20_10_28_03_21_02_07_01_14_01_11 = (
        XmlPeriod("--01-07"),
        XmlPeriod("--08-03"),
        XmlPeriod("--01-20"),
        XmlPeriod("--10-28"),
        XmlPeriod("--03-21"),
        XmlPeriod("--02-07"),
        XmlPeriod("--01-14"),
        XmlPeriod("--01-11"),
    )


@dataclass
class NistschemaSvIvListGMonthDayEnumeration1:
    class Meta:
        name = "NISTSchema-SV-IV-list-gMonthDay-enumeration-1"
        namespace = "NISTSchema-SV-IV-list-gMonthDay-enumeration-1-NS"

    value: Optional[NistschemaSvIvListGMonthDayEnumeration1Type] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
