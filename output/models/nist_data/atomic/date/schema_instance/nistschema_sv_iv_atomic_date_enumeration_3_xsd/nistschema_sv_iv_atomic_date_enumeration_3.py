from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-date-enumeration-3-NS"


class NistschemaSvIvAtomicDateEnumeration3Type(Enum):
    VALUE_2005_06_19 = XmlDate(2005, 6, 19)
    VALUE_1973_10_26 = XmlDate(1973, 10, 26)
    VALUE_1992_08_14 = XmlDate(1992, 8, 14)
    VALUE_1973_09_16 = XmlDate(1973, 9, 16)
    VALUE_1990_04_07 = XmlDate(1990, 4, 7)
    VALUE_1995_07_16 = XmlDate(1995, 7, 16)
    VALUE_1985_09_24 = XmlDate(1985, 9, 24)


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDateEnumeration3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-date-enumeration-3"
        namespace = "NISTSchema-SV-IV-atomic-date-enumeration-3-NS"

    value: NistschemaSvIvAtomicDateEnumeration3Type = field(
        metadata={
            "required": True,
        }
    )
