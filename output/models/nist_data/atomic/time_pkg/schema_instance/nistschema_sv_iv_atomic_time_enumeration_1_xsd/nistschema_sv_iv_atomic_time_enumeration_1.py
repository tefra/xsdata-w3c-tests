from dataclasses import dataclass, field
from datetime import time
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-time-enumeration-1-NS"


class NistschemaSvIvAtomicTimeEnumeration1Type(Enum):
    VALUE_01_44_56 = time(1, 44, 56)
    VALUE_07_44_41 = time(7, 44, 41)
    VALUE_05_55_52 = time(5, 55, 52)
    VALUE_21_59_07 = time(21, 59, 7)
    VALUE_12_41_23 = time(12, 41, 23)
    VALUE_02_47_45 = time(2, 47, 45)
    VALUE_03_43_07 = time(3, 43, 7)
    VALUE_02_00_14 = time(2, 0, 14)
    VALUE_01_42_27 = time(1, 42, 27)


@dataclass
class NistschemaSvIvAtomicTimeEnumeration1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-time-enumeration-1"
        namespace = "NISTSchema-SV-IV-atomic-time-enumeration-1-NS"

    value: Optional[NistschemaSvIvAtomicTimeEnumeration1Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
