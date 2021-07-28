from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-list-gMonth-enumeration-2-NS"


class NistschemaSvIvListGMonthEnumeration2Type(Enum):
    VALUE_12_08_08_06_08_11_09_12_05_09 = (
            XmlPeriod("--12"),
            XmlPeriod("--08"),
            XmlPeriod("--08"),
            XmlPeriod("--06"),
            XmlPeriod("--08"),
            XmlPeriod("--11"),
            XmlPeriod("--09"),
            XmlPeriod("--12"),
            XmlPeriod("--05"),
            XmlPeriod("--09"),
        )
    VALUE_06_10_10_08_07_07_04_11_02 = (
            XmlPeriod("--06"),
            XmlPeriod("--10"),
            XmlPeriod("--10"),
            XmlPeriod("--08"),
            XmlPeriod("--07"),
            XmlPeriod("--07"),
            XmlPeriod("--04"),
            XmlPeriod("--11"),
            XmlPeriod("--02"),
        )
    VALUE_09_09_09_06_01_04_01_09 = (
            XmlPeriod("--09"),
            XmlPeriod("--09"),
            XmlPeriod("--09"),
            XmlPeriod("--06"),
            XmlPeriod("--01"),
            XmlPeriod("--04"),
            XmlPeriod("--01"),
            XmlPeriod("--09"),
        )
    VALUE_06_11_11_06_02_04_01_05_06 = (
            XmlPeriod("--06"),
            XmlPeriod("--11"),
            XmlPeriod("--11"),
            XmlPeriod("--06"),
            XmlPeriod("--02"),
            XmlPeriod("--04"),
            XmlPeriod("--01"),
            XmlPeriod("--05"),
            XmlPeriod("--06"),
        )
    VALUE_07_08_01_06_07 = (
            XmlPeriod("--07"),
            XmlPeriod("--08"),
            XmlPeriod("--01"),
            XmlPeriod("--06"),
            XmlPeriod("--07"),
        )
    VALUE_11_07_12_09_09_09_01_10 = (
            XmlPeriod("--11"),
            XmlPeriod("--07"),
            XmlPeriod("--12"),
            XmlPeriod("--09"),
            XmlPeriod("--09"),
            XmlPeriod("--09"),
            XmlPeriod("--01"),
            XmlPeriod("--10"),
        )
    VALUE_02_08_08_07_02_09_02 = (
            XmlPeriod("--02"),
            XmlPeriod("--08"),
            XmlPeriod("--08"),
            XmlPeriod("--07"),
            XmlPeriod("--02"),
            XmlPeriod("--09"),
            XmlPeriod("--02"),
        )
    VALUE_05_04_01_03_11_04_01_10_06 = (
            XmlPeriod("--05"),
            XmlPeriod("--04"),
            XmlPeriod("--01"),
            XmlPeriod("--03"),
            XmlPeriod("--11"),
            XmlPeriod("--04"),
            XmlPeriod("--01"),
            XmlPeriod("--10"),
            XmlPeriod("--06"),
        )


@dataclass
class NistschemaSvIvListGMonthEnumeration2:
    class Meta:
        name = "NISTSchema-SV-IV-list-gMonth-enumeration-2"
        namespace = "NISTSchema-SV-IV-list-gMonth-enumeration-2-NS"

    value: Optional[NistschemaSvIvListGMonthEnumeration2Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
