from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from xsdata.models.datatype import XmlTime

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-time-enumeration-3-NS"


class NistschemaSvIvAtomicTimeEnumeration3Type(Enum):
    VALUE_03_47_11 = XmlTime(3, 47, 11, 0)
    VALUE_16_04_46 = XmlTime(16, 4, 46, 0)
    VALUE_01_35_26 = XmlTime(1, 35, 26, 0)
    VALUE_22_39_51 = XmlTime(22, 39, 51, 0)
    VALUE_15_13_10 = XmlTime(15, 13, 10, 0)
    VALUE_23_32_59 = XmlTime(23, 32, 59, 0)
    VALUE_02_39_19 = XmlTime(2, 39, 19, 0)


@dataclass(kw_only=True)
class NistschemaSvIvAtomicTimeEnumeration3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-time-enumeration-3"
        namespace = "NISTSchema-SV-IV-atomic-time-enumeration-3-NS"

    value: NistschemaSvIvAtomicTimeEnumeration3Type = field()
