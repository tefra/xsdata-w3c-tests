from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-list-gMonth-enumeration-3-NS"


class NistschemaSvIvListGMonthEnumeration3Type(Enum):
    VALUE_10_06_07_10_02_04_07 = (
            XmlPeriod("--10"),
            XmlPeriod("--06"),
            XmlPeriod("--07"),
            XmlPeriod("--10"),
            XmlPeriod("--02"),
            XmlPeriod("--04"),
            XmlPeriod("--07"),
        )
    VALUE_12_04_08_08_08_08_04 = (
            XmlPeriod("--12"),
            XmlPeriod("--04"),
            XmlPeriod("--08"),
            XmlPeriod("--08"),
            XmlPeriod("--08"),
            XmlPeriod("--08"),
            XmlPeriod("--04"),
        )
    VALUE_09_04_02_12_08_03_02_01 = (
            XmlPeriod("--09"),
            XmlPeriod("--04"),
            XmlPeriod("--02"),
            XmlPeriod("--12"),
            XmlPeriod("--08"),
            XmlPeriod("--03"),
            XmlPeriod("--02"),
            XmlPeriod("--01"),
        )
    VALUE_02_11_06_07_02_08_01_06_07 = (
            XmlPeriod("--02"),
            XmlPeriod("--11"),
            XmlPeriod("--06"),
            XmlPeriod("--07"),
            XmlPeriod("--02"),
            XmlPeriod("--08"),
            XmlPeriod("--01"),
            XmlPeriod("--06"),
            XmlPeriod("--07"),
        )
    VALUE_02_05_10_03_09_02_04_09 = (
            XmlPeriod("--02"),
            XmlPeriod("--05"),
            XmlPeriod("--10"),
            XmlPeriod("--03"),
            XmlPeriod("--09"),
            XmlPeriod("--02"),
            XmlPeriod("--04"),
            XmlPeriod("--09"),
        )
    VALUE_12_10_12_09_09_04_04 = (
            XmlPeriod("--12"),
            XmlPeriod("--10"),
            XmlPeriod("--12"),
            XmlPeriod("--09"),
            XmlPeriod("--09"),
            XmlPeriod("--04"),
            XmlPeriod("--04"),
        )
    VALUE_11_02_02_05_10_05 = (
            XmlPeriod("--11"),
            XmlPeriod("--02"),
            XmlPeriod("--02"),
            XmlPeriod("--05"),
            XmlPeriod("--10"),
            XmlPeriod("--05"),
        )
    VALUE_02_05_09_09_02_04 = (
            XmlPeriod("--02"),
            XmlPeriod("--05"),
            XmlPeriod("--09"),
            XmlPeriod("--09"),
            XmlPeriod("--02"),
            XmlPeriod("--04"),
        )
    VALUE_04_03_02_06_06_06_08 = (
            XmlPeriod("--04"),
            XmlPeriod("--03"),
            XmlPeriod("--02"),
            XmlPeriod("--06"),
            XmlPeriod("--06"),
            XmlPeriod("--06"),
            XmlPeriod("--08"),
        )
    VALUE_04_08_03_06_10 = (
            XmlPeriod("--04"),
            XmlPeriod("--08"),
            XmlPeriod("--03"),
            XmlPeriod("--06"),
            XmlPeriod("--10"),
        )


@dataclass
class NistschemaSvIvListGMonthEnumeration3:
    class Meta:
        name = "NISTSchema-SV-IV-list-gMonth-enumeration-3"
        namespace = "NISTSchema-SV-IV-list-gMonth-enumeration-3-NS"

    value: Optional[NistschemaSvIvListGMonthEnumeration3Type] = field(
        default=None
    )
