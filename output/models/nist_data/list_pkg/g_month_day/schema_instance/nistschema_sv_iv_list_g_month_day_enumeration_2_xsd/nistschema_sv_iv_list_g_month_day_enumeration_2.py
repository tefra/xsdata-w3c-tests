from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-list-gMonthDay-enumeration-2-NS"


class NistschemaSvIvListGMonthDayEnumeration2Type(Enum):
    VALUE_11_10_03_26_08_04_12_23_02_11_06_02_08_06_07_10_05_18_08_10 = (
        XmlPeriod("--11-10"),
        XmlPeriod("--03-26"),
        XmlPeriod("--08-04"),
        XmlPeriod("--12-23"),
        XmlPeriod("--02-11"),
        XmlPeriod("--06-02"),
        XmlPeriod("--08-06"),
        XmlPeriod("--07-10"),
        XmlPeriod("--05-18"),
        XmlPeriod("--08-10"),
    )
    VALUE_07_24_08_04_10_05_11_19_08_05_03_06_10_17_08_11 = (
        XmlPeriod("--07-24"),
        XmlPeriod("--08-04"),
        XmlPeriod("--10-05"),
        XmlPeriod("--11-19"),
        XmlPeriod("--08-05"),
        XmlPeriod("--03-06"),
        XmlPeriod("--10-17"),
        XmlPeriod("--08-11"),
    )
    VALUE_03_21_11_21_03_15_03_20_12_13_10_26_11_15 = (
        XmlPeriod("--03-21"),
        XmlPeriod("--11-21"),
        XmlPeriod("--03-15"),
        XmlPeriod("--03-20"),
        XmlPeriod("--12-13"),
        XmlPeriod("--10-26"),
        XmlPeriod("--11-15"),
    )
    VALUE_01_24_09_05_09_29_04_28_10_01 = (
        XmlPeriod("--01-24"),
        XmlPeriod("--09-05"),
        XmlPeriod("--09-29"),
        XmlPeriod("--04-28"),
        XmlPeriod("--10-01"),
    )
    VALUE_08_01_05_03_12_09_08_13_09_10_01_09_11_06_03_07_01_28 = (
        XmlPeriod("--08-01"),
        XmlPeriod("--05-03"),
        XmlPeriod("--12-09"),
        XmlPeriod("--08-13"),
        XmlPeriod("--09-10"),
        XmlPeriod("--01-09"),
        XmlPeriod("--11-06"),
        XmlPeriod("--03-07"),
        XmlPeriod("--01-28"),
    )
    VALUE_11_16_10_05_04_18_09_19_11_13_05_03_06_13_02_25 = (
        XmlPeriod("--11-16"),
        XmlPeriod("--10-05"),
        XmlPeriod("--04-18"),
        XmlPeriod("--09-19"),
        XmlPeriod("--11-13"),
        XmlPeriod("--05-03"),
        XmlPeriod("--06-13"),
        XmlPeriod("--02-25"),
    )
    VALUE_06_08_03_26_03_22_01_27_03_20_06_08_01_10_07_17_03_02 = (
        XmlPeriod("--06-08"),
        XmlPeriod("--03-26"),
        XmlPeriod("--03-22"),
        XmlPeriod("--01-27"),
        XmlPeriod("--03-20"),
        XmlPeriod("--06-08"),
        XmlPeriod("--01-10"),
        XmlPeriod("--07-17"),
        XmlPeriod("--03-02"),
    )
    VALUE_03_18_12_15_06_19_12_09_01_28 = (
        XmlPeriod("--03-18"),
        XmlPeriod("--12-15"),
        XmlPeriod("--06-19"),
        XmlPeriod("--12-09"),
        XmlPeriod("--01-28"),
    )


@dataclass(kw_only=True)
class NistschemaSvIvListGMonthDayEnumeration2:
    class Meta:
        name = "NISTSchema-SV-IV-list-gMonthDay-enumeration-2"
        namespace = "NISTSchema-SV-IV-list-gMonthDay-enumeration-2-NS"

    value: NistschemaSvIvListGMonthDayEnumeration2Type = field(
        metadata={
            "required": True,
        }
    )
