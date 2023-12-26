from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xsdata.models.datatype import XmlTime

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-time-enumeration-1-NS"


class NistschemaSvIvAtomicTimeEnumeration1Type(Enum):
    VALUE_01_44_56 = XmlTime(1, 44, 56, 0)
    VALUE_07_44_41 = XmlTime(7, 44, 41, 0)
    VALUE_05_55_52 = XmlTime(5, 55, 52, 0)
    VALUE_21_59_07 = XmlTime(21, 59, 7, 0)
    VALUE_12_41_23 = XmlTime(12, 41, 23, 0)
    VALUE_02_47_45 = XmlTime(2, 47, 45, 0)
    VALUE_03_43_07 = XmlTime(3, 43, 7, 0)
    VALUE_02_00_14 = XmlTime(2, 0, 14, 0)
    VALUE_01_42_27 = XmlTime(1, 42, 27, 0)


@dataclass
class NistschemaSvIvAtomicTimeEnumeration1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-time-enumeration-1"
        namespace = "NISTSchema-SV-IV-atomic-time-enumeration-1-NS"

    value: Optional[NistschemaSvIvAtomicTimeEnumeration1Type] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
