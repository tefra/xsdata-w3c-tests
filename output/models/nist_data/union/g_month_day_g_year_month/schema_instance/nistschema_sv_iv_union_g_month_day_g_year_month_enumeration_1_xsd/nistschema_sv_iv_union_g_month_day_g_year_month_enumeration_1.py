from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-union-gMonthDay-gYearMonth-enumeration-1-NS"


class NistschemaSvIvUnionGMonthDayGYearMonthEnumeration1Type(Enum):
    VALUE_04_23 = XmlPeriod("--04-23")
    VALUE_1989_09 = XmlPeriod("1989-09")
    VALUE_2015_07 = XmlPeriod("2015-07")
    VALUE_11_30 = XmlPeriod("--11-30")
    VALUE_2003_07 = XmlPeriod("2003-07")
    VALUE_1994_09 = XmlPeriod("1994-09")
    VALUE_2023_02 = XmlPeriod("2023-02")
    VALUE_1982_09 = XmlPeriod("1982-09")


@dataclass
class NistschemaSvIvUnionGMonthDayGYearMonthEnumeration1:
    class Meta:
        name = "NISTSchema-SV-IV-union-gMonthDay-gYearMonth-enumeration-1"
        namespace = "NISTSchema-SV-IV-union-gMonthDay-gYearMonth-enumeration-1-NS"

    value: Optional[NistschemaSvIvUnionGMonthDayGYearMonthEnumeration1Type] = field(
        default=None
    )
