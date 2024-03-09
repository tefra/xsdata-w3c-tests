from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-date-enumeration-1-NS"


class NistschemaSvIvAtomicDateEnumeration1Type(Enum):
    VALUE_1975_06_11 = XmlDate(1975, 6, 11)
    VALUE_1997_12_26 = XmlDate(1997, 12, 26)
    VALUE_1998_11_16 = XmlDate(1998, 11, 16)
    VALUE_2023_08_17 = XmlDate(2023, 8, 17)
    VALUE_2010_04_24 = XmlDate(2010, 4, 24)
    VALUE_2028_06_23 = XmlDate(2028, 6, 23)
    VALUE_2015_03_13 = XmlDate(2015, 3, 13)
    VALUE_2026_01_04 = XmlDate(2026, 1, 4)


@dataclass
class NistschemaSvIvAtomicDateEnumeration1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-date-enumeration-1"
        namespace = "NISTSchema-SV-IV-atomic-date-enumeration-1-NS"

    value: Optional[NistschemaSvIvAtomicDateEnumeration1Type] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
