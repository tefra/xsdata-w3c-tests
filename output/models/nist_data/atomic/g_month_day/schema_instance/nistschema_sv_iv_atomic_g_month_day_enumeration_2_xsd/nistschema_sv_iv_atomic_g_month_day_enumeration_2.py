from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gMonthDay-enumeration-2-NS"


class NistschemaSvIvAtomicGMonthDayEnumeration2Type(Enum):
    VALUE_09_24 = XmlPeriod("--09-24")
    VALUE_01_28 = XmlPeriod("--01-28")
    VALUE_08_31 = XmlPeriod("--08-31")
    VALUE_08_20 = XmlPeriod("--08-20")
    VALUE_12_06 = XmlPeriod("--12-06")


@dataclass
class NistschemaSvIvAtomicGMonthDayEnumeration2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gMonthDay-enumeration-2"
        namespace = "NISTSchema-SV-IV-atomic-gMonthDay-enumeration-2-NS"

    value: Optional[NistschemaSvIvAtomicGMonthDayEnumeration2Type] = field(
        default=None
    )
