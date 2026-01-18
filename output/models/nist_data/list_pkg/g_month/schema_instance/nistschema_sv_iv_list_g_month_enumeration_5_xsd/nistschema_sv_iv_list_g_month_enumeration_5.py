from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-list-gMonth-enumeration-5-NS"


class NistschemaSvIvListGMonthEnumeration5Type(Enum):
    VALUE_07_12_12_03_01_11_01_05_03 = (
        XmlPeriod("--07"),
        XmlPeriod("--12"),
        XmlPeriod("--12"),
        XmlPeriod("--03"),
        XmlPeriod("--01"),
        XmlPeriod("--11"),
        XmlPeriod("--01"),
        XmlPeriod("--05"),
        XmlPeriod("--03"),
    )
    VALUE_04_05_04_10_06_08_03 = (
        XmlPeriod("--04"),
        XmlPeriod("--05"),
        XmlPeriod("--04"),
        XmlPeriod("--10"),
        XmlPeriod("--06"),
        XmlPeriod("--08"),
        XmlPeriod("--03"),
    )
    VALUE_11_07_07_02_06_02 = (
        XmlPeriod("--11"),
        XmlPeriod("--07"),
        XmlPeriod("--07"),
        XmlPeriod("--02"),
        XmlPeriod("--06"),
        XmlPeriod("--02"),
    )
    VALUE_11_11_04_09_03_10_05_03 = (
        XmlPeriod("--11"),
        XmlPeriod("--11"),
        XmlPeriod("--04"),
        XmlPeriod("--09"),
        XmlPeriod("--03"),
        XmlPeriod("--10"),
        XmlPeriod("--05"),
        XmlPeriod("--03"),
    )
    VALUE_03_09_07_07_10_07_08_11_08_03 = (
        XmlPeriod("--03"),
        XmlPeriod("--09"),
        XmlPeriod("--07"),
        XmlPeriod("--07"),
        XmlPeriod("--10"),
        XmlPeriod("--07"),
        XmlPeriod("--08"),
        XmlPeriod("--11"),
        XmlPeriod("--08"),
        XmlPeriod("--03"),
    )
    VALUE_03_02_01_05_08_04_02_07 = (
        XmlPeriod("--03"),
        XmlPeriod("--02"),
        XmlPeriod("--01"),
        XmlPeriod("--05"),
        XmlPeriod("--08"),
        XmlPeriod("--04"),
        XmlPeriod("--02"),
        XmlPeriod("--07"),
    )


@dataclass(kw_only=True)
class NistschemaSvIvListGMonthEnumeration5:
    class Meta:
        name = "NISTSchema-SV-IV-list-gMonth-enumeration-5"
        namespace = "NISTSchema-SV-IV-list-gMonth-enumeration-5-NS"

    value: NistschemaSvIvListGMonthEnumeration5Type = field(
        metadata={
            "required": True,
        }
    )
