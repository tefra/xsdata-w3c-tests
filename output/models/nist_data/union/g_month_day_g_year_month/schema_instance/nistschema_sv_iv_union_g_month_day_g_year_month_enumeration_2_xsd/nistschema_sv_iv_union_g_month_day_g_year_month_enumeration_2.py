from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-union-gMonthDay-gYearMonth-enumeration-2-NS"


class NistschemaSvIvUnionGMonthDayGYearMonthEnumeration2Type(Enum):
    VALUE_05_21 = XmlPeriod("--05-21")
    VALUE_2005_08 = XmlPeriod("2005-08")
    VALUE_10_17 = XmlPeriod("--10-17")
    VALUE_1995_07 = XmlPeriod("1995-07")
    VALUE_1984_12 = XmlPeriod("1984-12")
    VALUE_06_14 = XmlPeriod("--06-14")
    VALUE_1994_09 = XmlPeriod("1994-09")
    VALUE_1980_05 = XmlPeriod("1980-05")


@dataclass(kw_only=True)
class NistschemaSvIvUnionGMonthDayGYearMonthEnumeration2:
    class Meta:
        name = "NISTSchema-SV-IV-union-gMonthDay-gYearMonth-enumeration-2"
        namespace = (
            "NISTSchema-SV-IV-union-gMonthDay-gYearMonth-enumeration-2-NS"
        )

    value: NistschemaSvIvUnionGMonthDayGYearMonthEnumeration2Type = field(
        metadata={
            "required": True,
        }
    )
