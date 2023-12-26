from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-dateTime-enumeration-2-NS"


class NistschemaSvIvAtomicDateTimeEnumeration2Type(Enum):
    VALUE_2016_12_24_T10_20_27 = XmlDateTime(2016, 12, 24, 10, 20, 27)
    VALUE_2013_04_14_T17_20_13 = XmlDateTime(2013, 4, 14, 17, 20, 13)
    VALUE_1997_07_18_T03_59_37 = XmlDateTime(1997, 7, 18, 3, 59, 37)
    VALUE_2004_04_06_T20_47_16 = XmlDateTime(2004, 4, 6, 20, 47, 16)
    VALUE_2024_07_02_T09_44_13 = XmlDateTime(2024, 7, 2, 9, 44, 13)
    VALUE_1980_08_25_T23_48_17 = XmlDateTime(1980, 8, 25, 23, 48, 17)


@dataclass
class NistschemaSvIvAtomicDateTimeEnumeration2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-dateTime-enumeration-2"
        namespace = "NISTSchema-SV-IV-atomic-dateTime-enumeration-2-NS"

    value: Optional[NistschemaSvIvAtomicDateTimeEnumeration2Type] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
