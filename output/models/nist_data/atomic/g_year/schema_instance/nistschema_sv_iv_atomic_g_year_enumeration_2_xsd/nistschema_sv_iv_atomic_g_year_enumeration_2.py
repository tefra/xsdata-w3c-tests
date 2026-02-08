from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYear-enumeration-2-NS"


class NistschemaSvIvAtomicGYearEnumeration2Type(Enum):
    VALUE_2007 = XmlPeriod("2007")
    VALUE_2020 = XmlPeriod("2020")
    VALUE_1999 = XmlPeriod("1999")
    VALUE_2011 = XmlPeriod("2011")
    VALUE_1976 = XmlPeriod("1976")
    VALUE_1984 = XmlPeriod("1984")
    VALUE_1972 = XmlPeriod("1972")
    VALUE_1992 = XmlPeriod("1992")
    VALUE_2018 = XmlPeriod("2018")


@dataclass(kw_only=True)
class NistschemaSvIvAtomicGYearEnumeration2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYear-enumeration-2"
        namespace = "NISTSchema-SV-IV-atomic-gYear-enumeration-2-NS"

    value: NistschemaSvIvAtomicGYearEnumeration2Type = field()
