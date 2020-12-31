from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xsdata.models.datatype import Period

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gMonthDay-enumeration-1-NS"


class NistschemaSvIvAtomicGMonthDayEnumeration1Type(Enum):
    VALUE_08_18 = Period("--08-18")
    VALUE_08_19 = Period("--08-19")
    VALUE_05_19 = Period("--05-19")
    VALUE_11_08 = Period("--11-08")
    VALUE_09_16 = Period("--09-16")
    VALUE_05_29 = Period("--05-29")
    VALUE_11_18 = Period("--11-18")
    VALUE_07_05 = Period("--07-05")


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
