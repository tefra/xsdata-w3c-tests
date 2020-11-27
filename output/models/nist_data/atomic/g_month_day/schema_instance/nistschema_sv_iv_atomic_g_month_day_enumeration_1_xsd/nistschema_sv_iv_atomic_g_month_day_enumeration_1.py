from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gMonthDay-enumeration-1-NS"


class NistschemaSvIvAtomicGMonthDayEnumeration1Type(Enum):
    VALUE_08_18 = "--08-18"
    VALUE_08_19 = "--08-19"
    VALUE_05_19 = "--05-19"
    VALUE_11_08 = "--11-08"
    VALUE_09_16 = "--09-16"
    VALUE_05_29 = "--05-29"
    VALUE_11_18 = "--11-18"
    VALUE_07_05 = "--07-05"


@dataclass
class NistschemaSvIvAtomicGMonthDayEnumeration1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gMonthDay-enumeration-1"
        namespace = "NISTSchema-SV-IV-atomic-gMonthDay-enumeration-1-NS"

    value: Optional[NistschemaSvIvAtomicGMonthDayEnumeration1Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
