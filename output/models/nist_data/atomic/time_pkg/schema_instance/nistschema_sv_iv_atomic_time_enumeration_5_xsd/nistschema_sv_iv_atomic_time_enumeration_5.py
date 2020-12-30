from dataclasses import dataclass, field
from datetime import time
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-time-enumeration-5-NS"


class NistschemaSvIvAtomicTimeEnumeration5Type(Enum):
    VALUE_06_18_04 = time(6, 18, 4)
    VALUE_07_45_10 = time(7, 45, 10)
    VALUE_12_06_46 = time(12, 6, 46)
    VALUE_21_01_58 = time(21, 1, 58)
    VALUE_05_34_33 = time(5, 34, 33)
    VALUE_22_22_06 = time(22, 22, 6)
    VALUE_12_17_04 = time(12, 17, 4)


@dataclass
class NistschemaSvIvAtomicTimeEnumeration5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-time-enumeration-5"
        namespace = "NISTSchema-SV-IV-atomic-time-enumeration-5-NS"

    value: Optional[NistschemaSvIvAtomicTimeEnumeration5Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
