from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from xsdata.models.datatype import XmlTime

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-time-enumeration-4-NS"


class NistschemaSvIvAtomicTimeEnumeration4Type(Enum):
    VALUE_18_04_07 = XmlTime(18, 4, 7, 0)
    VALUE_05_41_14 = XmlTime(5, 41, 14, 0)
    VALUE_15_07_15 = XmlTime(15, 7, 15, 0)
    VALUE_01_18_17 = XmlTime(1, 18, 17, 0)
    VALUE_01_13_21 = XmlTime(1, 13, 21, 0)
    VALUE_23_24_35 = XmlTime(23, 24, 35, 0)
    VALUE_15_25_08 = XmlTime(15, 25, 8, 0)
    VALUE_18_20_35 = XmlTime(18, 20, 35, 0)
    VALUE_03_53_17 = XmlTime(3, 53, 17, 0)


@dataclass(kw_only=True)
class NistschemaSvIvAtomicTimeEnumeration4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-time-enumeration-4"
        namespace = "NISTSchema-SV-IV-atomic-time-enumeration-4-NS"

    value: NistschemaSvIvAtomicTimeEnumeration4Type = field(
        metadata={
            "required": True,
        }
    )
