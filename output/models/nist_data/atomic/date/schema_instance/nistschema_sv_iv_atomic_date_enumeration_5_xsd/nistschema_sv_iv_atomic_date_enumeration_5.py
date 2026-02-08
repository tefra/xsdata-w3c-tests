from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-date-enumeration-5-NS"


class NistschemaSvIvAtomicDateEnumeration5Type(Enum):
    VALUE_1972_02_04 = XmlDate(1972, 2, 4)
    VALUE_2010_06_24 = XmlDate(2010, 6, 24)
    VALUE_2022_08_04 = XmlDate(2022, 8, 4)
    VALUE_2006_12_31 = XmlDate(2006, 12, 31)
    VALUE_1992_01_14 = XmlDate(1992, 1, 14)
    VALUE_2027_09_16 = XmlDate(2027, 9, 16)
    VALUE_1980_07_02 = XmlDate(1980, 7, 2)
    VALUE_2013_06_03 = XmlDate(2013, 6, 3)


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDateEnumeration5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-date-enumeration-5"
        namespace = "NISTSchema-SV-IV-atomic-date-enumeration-5-NS"

    value: NistschemaSvIvAtomicDateEnumeration5Type = field()
