from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-list-gMonth-enumeration-4-NS"


class NistschemaSvIvListGMonthEnumeration4Type(Enum):
    VALUE_08_10_09_10_04_07_10_01_01 = (
            XmlPeriod("--08"),
            XmlPeriod("--10"),
            XmlPeriod("--09"),
            XmlPeriod("--10"),
            XmlPeriod("--04"),
            XmlPeriod("--07"),
            XmlPeriod("--10"),
            XmlPeriod("--01"),
            XmlPeriod("--01"),
        )
    VALUE_03_06_11_09_02_08 = (
            XmlPeriod("--03"),
            XmlPeriod("--06"),
            XmlPeriod("--11"),
            XmlPeriod("--09"),
            XmlPeriod("--02"),
            XmlPeriod("--08"),
        )
    VALUE_08_05_07_07_02_11_09 = (
            XmlPeriod("--08"),
            XmlPeriod("--05"),
            XmlPeriod("--07"),
            XmlPeriod("--07"),
            XmlPeriod("--02"),
            XmlPeriod("--11"),
            XmlPeriod("--09"),
        )
    VALUE_06_08_04_09_06_10_09_01 = (
            XmlPeriod("--06"),
            XmlPeriod("--08"),
            XmlPeriod("--04"),
            XmlPeriod("--09"),
            XmlPeriod("--06"),
            XmlPeriod("--10"),
            XmlPeriod("--09"),
            XmlPeriod("--01"),
        )
    VALUE_09_01_04_08_09_06_07_11_08 = (
            XmlPeriod("--09"),
            XmlPeriod("--01"),
            XmlPeriod("--04"),
            XmlPeriod("--08"),
            XmlPeriod("--09"),
            XmlPeriod("--06"),
            XmlPeriod("--07"),
            XmlPeriod("--11"),
            XmlPeriod("--08"),
        )


@dataclass
class NistschemaSvIvListGMonthEnumeration4:
    class Meta:
        name = "NISTSchema-SV-IV-list-gMonth-enumeration-4"
        namespace = "NISTSchema-SV-IV-list-gMonth-enumeration-4-NS"

    value: Optional[NistschemaSvIvListGMonthEnumeration4Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
