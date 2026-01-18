from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYearMonth-enumeration-3-NS"


class NistschemaSvIvAtomicGYearMonthEnumeration3Type(Enum):
    VALUE_1978_12 = XmlPeriod("1978-12")
    VALUE_2002_12 = XmlPeriod("2002-12")
    VALUE_2001_09 = XmlPeriod("2001-09")
    VALUE_1972_08 = XmlPeriod("1972-08")
    VALUE_1973_09 = XmlPeriod("1973-09")


@dataclass(kw_only=True)
class NistschemaSvIvAtomicGYearMonthEnumeration3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYearMonth-enumeration-3"
        namespace = "NISTSchema-SV-IV-atomic-gYearMonth-enumeration-3-NS"

    value: NistschemaSvIvAtomicGYearMonthEnumeration3Type = field(
        metadata={
            "required": True,
        }
    )
