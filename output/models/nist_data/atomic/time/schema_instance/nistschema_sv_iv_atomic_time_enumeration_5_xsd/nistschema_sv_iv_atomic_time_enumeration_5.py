from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

from xsdata.models.datatype import XmlTime

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-time-enumeration-5-NS"


class NistschemaSvIvAtomicTimeEnumeration5Type(Enum):
    VALUE_06_18_04 = XmlTime(6, 18, 4, 0)
    VALUE_07_45_10 = XmlTime(7, 45, 10, 0)
    VALUE_12_06_46 = XmlTime(12, 6, 46, 0)
    VALUE_21_01_58 = XmlTime(21, 1, 58, 0)
    VALUE_05_34_33 = XmlTime(5, 34, 33, 0)
    VALUE_22_22_06 = XmlTime(22, 22, 6, 0)
    VALUE_12_17_04 = XmlTime(12, 17, 4, 0)


@dataclass
class NistschemaSvIvAtomicTimeEnumeration5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-time-enumeration-5"
        namespace = "NISTSchema-SV-IV-atomic-time-enumeration-5-NS"

    value: Optional[NistschemaSvIvAtomicTimeEnumeration5Type] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
