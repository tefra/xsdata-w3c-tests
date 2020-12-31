from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xsdata.models.datatype import Period

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gMonthDay-enumeration-2-NS"


class NistschemaSvIvAtomicGMonthDayEnumeration2Type(Enum):
    VALUE_09_24 = Period("--09-24")
    VALUE_01_28 = Period("--01-28")
    VALUE_08_31 = Period("--08-31")
    VALUE_08_20 = Period("--08-20")
    VALUE_12_06 = Period("--12-06")


@dataclass
class NistschemaSvIvAtomicGMonthDayEnumeration2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gMonthDay-enumeration-2"
        namespace = "NISTSchema-SV-IV-atomic-gMonthDay-enumeration-2-NS"

    value: Optional[NistschemaSvIvAtomicGMonthDayEnumeration2Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
