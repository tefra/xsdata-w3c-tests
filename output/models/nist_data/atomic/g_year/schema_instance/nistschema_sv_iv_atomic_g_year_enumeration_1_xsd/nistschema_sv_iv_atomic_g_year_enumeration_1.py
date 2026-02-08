from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYear-enumeration-1-NS"


class NistschemaSvIvAtomicGYearEnumeration1Type(Enum):
    VALUE_2028 = XmlPeriod("2028")
    VALUE_1999 = XmlPeriod("1999")
    VALUE_1998 = XmlPeriod("1998")
    VALUE_1995 = XmlPeriod("1995")
    VALUE_2021 = XmlPeriod("2021")
    VALUE_2006 = XmlPeriod("2006")
    VALUE_2007 = XmlPeriod("2007")
    VALUE_2015 = XmlPeriod("2015")


@dataclass(kw_only=True)
class NistschemaSvIvAtomicGYearEnumeration1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYear-enumeration-1"
        namespace = "NISTSchema-SV-IV-atomic-gYear-enumeration-1-NS"

    value: NistschemaSvIvAtomicGYearEnumeration1Type = field()
