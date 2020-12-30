from dataclasses import dataclass, field
from datetime import time
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-time-enumeration-4-NS"


class NistschemaSvIvAtomicTimeEnumeration4Type(Enum):
    VALUE_18_04_07 = time(18, 4, 7)
    VALUE_05_41_14 = time(5, 41, 14)
    VALUE_15_07_15 = time(15, 7, 15)
    VALUE_01_18_17 = time(1, 18, 17)
    VALUE_01_13_21 = time(1, 13, 21)
    VALUE_23_24_35 = time(23, 24, 35)
    VALUE_15_25_08 = time(15, 25, 8)
    VALUE_18_20_35 = time(18, 20, 35)
    VALUE_03_53_17 = time(3, 53, 17)


@dataclass
class NistschemaSvIvAtomicTimeEnumeration4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-time-enumeration-4"
        namespace = "NISTSchema-SV-IV-atomic-time-enumeration-4-NS"

    value: Optional[NistschemaSvIvAtomicTimeEnumeration4Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
