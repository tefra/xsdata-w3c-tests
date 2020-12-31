from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xsdata.models.datatype import Period

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gMonthDay-enumeration-4-NS"


class NistschemaSvIvAtomicGMonthDayEnumeration4Type(Enum):
    VALUE_06_07 = Period("--06-07")
    VALUE_11_20 = Period("--11-20")
    VALUE_01_29 = Period("--01-29")
    VALUE_11_11 = Period("--11-11")
    VALUE_11_17 = Period("--11-17")
    VALUE_05_08 = Period("--05-08")
    VALUE_07_06 = Period("--07-06")
    VALUE_12_01 = Period("--12-01")
    VALUE_05_07 = Period("--05-07")
    VALUE_09_03 = Period("--09-03")


@dataclass
class NistschemaSvIvAtomicGMonthDayEnumeration4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gMonthDay-enumeration-4"
        namespace = "NISTSchema-SV-IV-atomic-gMonthDay-enumeration-4-NS"

    value: Optional[NistschemaSvIvAtomicGMonthDayEnumeration4Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
