from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-date-enumeration-2-NS"


class NistschemaSvIvAtomicDateEnumeration2Type(Enum):
    VALUE_2013_10_28 = XmlDate(2013, 10, 28)
    VALUE_2009_09_16 = XmlDate(2009, 9, 16)
    VALUE_1974_02_14 = XmlDate(1974, 2, 14)
    VALUE_2027_04_22 = XmlDate(2027, 4, 22)
    VALUE_2027_07_03 = XmlDate(2027, 7, 3)
    VALUE_2001_08_03 = XmlDate(2001, 8, 3)
    VALUE_2015_12_10 = XmlDate(2015, 12, 10)


@dataclass
class NistschemaSvIvAtomicDateEnumeration2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-date-enumeration-2"
        namespace = "NISTSchema-SV-IV-atomic-date-enumeration-2-NS"

    value: Optional[NistschemaSvIvAtomicDateEnumeration2Type] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
