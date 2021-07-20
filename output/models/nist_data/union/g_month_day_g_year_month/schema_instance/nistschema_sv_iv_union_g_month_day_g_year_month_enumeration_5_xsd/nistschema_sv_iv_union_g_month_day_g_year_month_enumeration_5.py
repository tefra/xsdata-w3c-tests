from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-union-gMonthDay-gYearMonth-enumeration-5-NS"


class NistschemaSvIvUnionGMonthDayGYearMonthEnumeration5Type(Enum):
    VALUE_05_07 = XmlPeriod("--05-07")
    VALUE_07_18 = XmlPeriod("--07-18")
    VALUE_2011_09 = XmlPeriod("2011-09")
    VALUE_2019_10 = XmlPeriod("2019-10")
    VALUE_03_13 = XmlPeriod("--03-13")
    VALUE_02_15 = XmlPeriod("--02-15")
    VALUE_11_30 = XmlPeriod("--11-30")
    VALUE_1997_02 = XmlPeriod("1997-02")


@dataclass
class NistschemaSvIvUnionGMonthDayGYearMonthEnumeration5:
    class Meta:
        name = "NISTSchema-SV-IV-union-gMonthDay-gYearMonth-enumeration-5"
        namespace = "NISTSchema-SV-IV-union-gMonthDay-gYearMonth-enumeration-5-NS"

    value: Optional[NistschemaSvIvUnionGMonthDayGYearMonthEnumeration5Type] = field(
        default=None
    )
