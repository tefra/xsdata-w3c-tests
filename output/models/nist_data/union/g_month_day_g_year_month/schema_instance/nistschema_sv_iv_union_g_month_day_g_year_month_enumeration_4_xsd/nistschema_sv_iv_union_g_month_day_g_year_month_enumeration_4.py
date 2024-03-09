from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-union-gMonthDay-gYearMonth-enumeration-4-NS"


class NistschemaSvIvUnionGMonthDayGYearMonthEnumeration4Type(Enum):
    VALUE_1989_06 = XmlPeriod("1989-06")
    VALUE_2003_07 = XmlPeriod("2003-07")
    VALUE_12_24 = XmlPeriod("--12-24")
    VALUE_01_01 = XmlPeriod("--01-01")
    VALUE_2005_08 = XmlPeriod("2005-08")
    VALUE_04_02 = XmlPeriod("--04-02")
    VALUE_11_30 = XmlPeriod("--11-30")
    VALUE_2011_09 = XmlPeriod("2011-09")


@dataclass
class NistschemaSvIvUnionGMonthDayGYearMonthEnumeration4:
    class Meta:
        name = "NISTSchema-SV-IV-union-gMonthDay-gYearMonth-enumeration-4"
        namespace = (
            "NISTSchema-SV-IV-union-gMonthDay-gYearMonth-enumeration-4-NS"
        )

    value: Optional[NistschemaSvIvUnionGMonthDayGYearMonthEnumeration4Type] = (
        field(
            default=None,
            metadata={
                "required": True,
            },
        )
    )
