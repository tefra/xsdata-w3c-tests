from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-list-gMonth-enumeration-1-NS"


class NistschemaSvIvListGMonthEnumeration1Type(Enum):
    VALUE_10_09_07_07_09_08_09 = (
            XmlPeriod("--10"),
            XmlPeriod("--09"),
            XmlPeriod("--07"),
            XmlPeriod("--07"),
            XmlPeriod("--09"),
            XmlPeriod("--08"),
            XmlPeriod("--09"),
        )
    VALUE_06_05_10_06_04_06_07_04_09_03 = (
            XmlPeriod("--06"),
            XmlPeriod("--05"),
            XmlPeriod("--10"),
            XmlPeriod("--06"),
            XmlPeriod("--04"),
            XmlPeriod("--06"),
            XmlPeriod("--07"),
            XmlPeriod("--04"),
            XmlPeriod("--09"),
            XmlPeriod("--03"),
        )
    VALUE_02_09_10_11_06_05_02 = (
            XmlPeriod("--02"),
            XmlPeriod("--09"),
            XmlPeriod("--10"),
            XmlPeriod("--11"),
            XmlPeriod("--06"),
            XmlPeriod("--05"),
            XmlPeriod("--02"),
        )
    VALUE_05_09_10_05_10_12_04 = (
            XmlPeriod("--05"),
            XmlPeriod("--09"),
            XmlPeriod("--10"),
            XmlPeriod("--05"),
            XmlPeriod("--10"),
            XmlPeriod("--12"),
            XmlPeriod("--04"),
        )
    VALUE_05_08_11_05_10_06_09_01_05_12 = (
            XmlPeriod("--05"),
            XmlPeriod("--08"),
            XmlPeriod("--11"),
            XmlPeriod("--05"),
            XmlPeriod("--10"),
            XmlPeriod("--06"),
            XmlPeriod("--09"),
            XmlPeriod("--01"),
            XmlPeriod("--05"),
            XmlPeriod("--12"),
        )
    VALUE_08_08_07_02_01_04_02_11_01_11 = (
            XmlPeriod("--08"),
            XmlPeriod("--08"),
            XmlPeriod("--07"),
            XmlPeriod("--02"),
            XmlPeriod("--01"),
            XmlPeriod("--04"),
            XmlPeriod("--02"),
            XmlPeriod("--11"),
            XmlPeriod("--01"),
            XmlPeriod("--11"),
        )
    VALUE_11_03_09_08_05_09_02_06_04 = (
            XmlPeriod("--11"),
            XmlPeriod("--03"),
            XmlPeriod("--09"),
            XmlPeriod("--08"),
            XmlPeriod("--05"),
            XmlPeriod("--09"),
            XmlPeriod("--02"),
            XmlPeriod("--06"),
            XmlPeriod("--04"),
        )


@dataclass
class NistschemaSvIvListGMonthEnumeration1:
    class Meta:
        name = "NISTSchema-SV-IV-list-gMonth-enumeration-1"
        namespace = "NISTSchema-SV-IV-list-gMonth-enumeration-1-NS"

    value: Optional[NistschemaSvIvListGMonthEnumeration1Type] = field(
        default=None
    )
