from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYear-enumeration-5-NS"


class NistschemaSvIvAtomicGYearEnumeration5Type(Enum):
    VALUE_2020 = XmlPeriod("2020")
    VALUE_1988 = XmlPeriod("1988")
    VALUE_1982 = XmlPeriod("1982")
    VALUE_2000 = XmlPeriod("2000")
    VALUE_1985 = XmlPeriod("1985")
    VALUE_1994 = XmlPeriod("1994")


@dataclass(kw_only=True)
class NistschemaSvIvAtomicGYearEnumeration5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYear-enumeration-5"
        namespace = "NISTSchema-SV-IV-atomic-gYear-enumeration-5-NS"

    value: NistschemaSvIvAtomicGYearEnumeration5Type = field(
        metadata={
            "required": True,
        }
    )
