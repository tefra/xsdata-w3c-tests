from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xsdata.models.datatype import Period

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gMonthDay-enumeration-3-NS"


class NistschemaSvIvAtomicGMonthDayEnumeration3Type(Enum):
    VALUE_12_23 = Period("--12-23")
    VALUE_07_11 = Period("--07-11")
    VALUE_06_24 = Period("--06-24")
    VALUE_10_27 = Period("--10-27")
    VALUE_09_07 = Period("--09-07")
    VALUE_03_29 = Period("--03-29")
    VALUE_12_01 = Period("--12-01")
    VALUE_01_29 = Period("--01-29")
    VALUE_07_09 = Period("--07-09")
    VALUE_10_05 = Period("--10-05")


@dataclass
class NistschemaSvIvAtomicGMonthDayEnumeration3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gMonthDay-enumeration-3"
        namespace = "NISTSchema-SV-IV-atomic-gMonthDay-enumeration-3-NS"

    value: Optional[NistschemaSvIvAtomicGMonthDayEnumeration3Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
