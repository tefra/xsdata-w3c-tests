from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYearMonth-enumeration-2-NS"


class NistschemaSvIvAtomicGYearMonthEnumeration2Type(Enum):
    VALUE_2017_08 = XmlPeriod("2017-08")
    VALUE_1986_04 = XmlPeriod("1986-04")
    VALUE_2000_01 = XmlPeriod("2000-01")
    VALUE_2015_06 = XmlPeriod("2015-06")
    VALUE_2010_09 = XmlPeriod("2010-09")
    VALUE_2002_07 = XmlPeriod("2002-07")
    VALUE_2020_10 = XmlPeriod("2020-10")
    VALUE_2012_02 = XmlPeriod("2012-02")


@dataclass(kw_only=True)
class NistschemaSvIvAtomicGYearMonthEnumeration2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYearMonth-enumeration-2"
        namespace = "NISTSchema-SV-IV-atomic-gYearMonth-enumeration-2-NS"

    value: NistschemaSvIvAtomicGYearMonthEnumeration2Type = field()
