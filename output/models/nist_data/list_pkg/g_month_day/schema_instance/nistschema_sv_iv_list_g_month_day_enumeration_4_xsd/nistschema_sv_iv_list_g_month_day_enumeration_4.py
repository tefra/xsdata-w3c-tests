from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-list-gMonthDay-enumeration-4-NS"


class NistschemaSvIvListGMonthDayEnumeration4Type(Enum):
    VALUE_10_08_05_11_06_17_06_19_06_21_04_09_12_29 = (
        XmlPeriod("--10-08"),
        XmlPeriod("--05-11"),
        XmlPeriod("--06-17"),
        XmlPeriod("--06-19"),
        XmlPeriod("--06-21"),
        XmlPeriod("--04-09"),
        XmlPeriod("--12-29"),
    )
    VALUE_09_16_02_01_09_05_01_17_02_04_10_11_05_27_03_01_04_26_09_02 = (
        XmlPeriod("--09-16"),
        XmlPeriod("--02-01"),
        XmlPeriod("--09-05"),
        XmlPeriod("--01-17"),
        XmlPeriod("--02-04"),
        XmlPeriod("--10-11"),
        XmlPeriod("--05-27"),
        XmlPeriod("--03-01"),
        XmlPeriod("--04-26"),
        XmlPeriod("--09-02"),
    )
    VALUE_09_02_04_08_01_01_07_02_07_05 = (
        XmlPeriod("--09-02"),
        XmlPeriod("--04-08"),
        XmlPeriod("--01-01"),
        XmlPeriod("--07-02"),
        XmlPeriod("--07-05"),
    )
    VALUE_05_11_06_11_07_22_05_17_02_01_09_18_05_01 = (
        XmlPeriod("--05-11"),
        XmlPeriod("--06-11"),
        XmlPeriod("--07-22"),
        XmlPeriod("--05-17"),
        XmlPeriod("--02-01"),
        XmlPeriod("--09-18"),
        XmlPeriod("--05-01"),
    )
    VALUE_10_30_09_02_01_03_08_15_09_07_12_28 = (
        XmlPeriod("--10-30"),
        XmlPeriod("--09-02"),
        XmlPeriod("--01-03"),
        XmlPeriod("--08-15"),
        XmlPeriod("--09-07"),
        XmlPeriod("--12-28"),
    )
    VALUE_11_23_09_21_06_05_04_28_08_06_04_16 = (
        XmlPeriod("--11-23"),
        XmlPeriod("--09-21"),
        XmlPeriod("--06-05"),
        XmlPeriod("--04-28"),
        XmlPeriod("--08-06"),
        XmlPeriod("--04-16"),
    )
    VALUE_11_05_05_25_02_01_03_10_02_12 = (
        XmlPeriod("--11-05"),
        XmlPeriod("--05-25"),
        XmlPeriod("--02-01"),
        XmlPeriod("--03-10"),
        XmlPeriod("--02-12"),
    )


@dataclass
class NistschemaSvIvListGMonthDayEnumeration4:
    class Meta:
        name = "NISTSchema-SV-IV-list-gMonthDay-enumeration-4"
        namespace = "NISTSchema-SV-IV-list-gMonthDay-enumeration-4-NS"

    value: Optional[NistschemaSvIvListGMonthDayEnumeration4Type] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
