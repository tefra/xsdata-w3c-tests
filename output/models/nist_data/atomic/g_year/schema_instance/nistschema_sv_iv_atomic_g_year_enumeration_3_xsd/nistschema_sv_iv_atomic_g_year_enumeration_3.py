from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYear-enumeration-3-NS"


class NistschemaSvIvAtomicGYearEnumeration3Type(Enum):
    VALUE_2004 = XmlPeriod("2004")
    VALUE_2014 = XmlPeriod("2014")
    VALUE_1991 = XmlPeriod("1991")
    VALUE_2001 = XmlPeriod("2001")
    VALUE_2021 = XmlPeriod("2021")


@dataclass(kw_only=True)
class NistschemaSvIvAtomicGYearEnumeration3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYear-enumeration-3"
        namespace = "NISTSchema-SV-IV-atomic-gYear-enumeration-3-NS"

    value: NistschemaSvIvAtomicGYearEnumeration3Type = field()
