from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-union-gMonthDay-gYearMonth-enumeration-3-NS"


class NistschemaSvIvUnionGMonthDayGYearMonthEnumeration3Type(Enum):
    VALUE_1990_11 = XmlPeriod("1990-11")
    VALUE_06_07 = XmlPeriod("--06-07")
    VALUE_2015_07 = XmlPeriod("2015-07")
    VALUE_01_10 = XmlPeriod("--01-10")
    VALUE_11_25 = XmlPeriod("--11-25")
    VALUE_2020_12 = XmlPeriod("2020-12")
    VALUE_08_04 = XmlPeriod("--08-04")
    VALUE_1980_06 = XmlPeriod("1980-06")
    VALUE_2011_09 = XmlPeriod("2011-09")


@dataclass
class NistschemaSvIvUnionGMonthDayGYearMonthEnumeration3:
    class Meta:
        name = "NISTSchema-SV-IV-union-gMonthDay-gYearMonth-enumeration-3"
        namespace = (
            "NISTSchema-SV-IV-union-gMonthDay-gYearMonth-enumeration-3-NS"
        )

    value: Optional[
        NistschemaSvIvUnionGMonthDayGYearMonthEnumeration3Type
    ] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
