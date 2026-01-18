from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-date-enumeration-4-NS"


class NistschemaSvIvAtomicDateEnumeration4Type(Enum):
    VALUE_1991_09_06 = XmlDate(1991, 9, 6)
    VALUE_2022_07_25 = XmlDate(2022, 7, 25)
    VALUE_2021_10_20 = XmlDate(2021, 10, 20)
    VALUE_1984_08_15 = XmlDate(1984, 8, 15)
    VALUE_1975_11_02 = XmlDate(1975, 11, 2)
    VALUE_2000_02_01 = XmlDate(2000, 2, 1)


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDateEnumeration4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-date-enumeration-4"
        namespace = "NISTSchema-SV-IV-atomic-date-enumeration-4-NS"

    value: NistschemaSvIvAtomicDateEnumeration4Type = field(
        metadata={
            "required": True,
        }
    )
