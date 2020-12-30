from dataclasses import dataclass, field
from datetime import time
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-time-enumeration-3-NS"


class NistschemaSvIvAtomicTimeEnumeration3Type(Enum):
    VALUE_03_47_11 = time(3, 47, 11)
    VALUE_16_04_46 = time(16, 4, 46)
    VALUE_01_35_26 = time(1, 35, 26)
    VALUE_22_39_51 = time(22, 39, 51)
    VALUE_15_13_10 = time(15, 13, 10)
    VALUE_23_32_59 = time(23, 32, 59)
    VALUE_02_39_19 = time(2, 39, 19)


@dataclass
class NistschemaSvIvAtomicTimeEnumeration3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-time-enumeration-3"
        namespace = "NISTSchema-SV-IV-atomic-time-enumeration-3-NS"

    value: Optional[NistschemaSvIvAtomicTimeEnumeration3Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
