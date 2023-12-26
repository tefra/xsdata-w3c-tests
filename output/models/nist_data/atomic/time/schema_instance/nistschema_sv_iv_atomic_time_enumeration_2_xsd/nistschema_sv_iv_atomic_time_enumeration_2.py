from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xsdata.models.datatype import XmlTime

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-time-enumeration-2-NS"


class NistschemaSvIvAtomicTimeEnumeration2Type(Enum):
    VALUE_10_32_33 = XmlTime(10, 32, 33, 0)
    VALUE_11_18_46 = XmlTime(11, 18, 46, 0)
    VALUE_06_00_33 = XmlTime(6, 0, 33, 0)
    VALUE_14_01_48 = XmlTime(14, 1, 48, 0)
    VALUE_11_14_02 = XmlTime(11, 14, 2, 0)
    VALUE_02_02_10 = XmlTime(2, 2, 10, 0)


@dataclass
class NistschemaSvIvAtomicTimeEnumeration2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-time-enumeration-2"
        namespace = "NISTSchema-SV-IV-atomic-time-enumeration-2-NS"

    value: Optional[NistschemaSvIvAtomicTimeEnumeration2Type] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
