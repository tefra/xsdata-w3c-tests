from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gMonthDay-enumeration-1-NS"


class NistschemaSvIvAtomicGMonthDayEnumeration1Type(Enum):
    VALUE_08_18 = XmlPeriod("--08-18")
    VALUE_08_19 = XmlPeriod("--08-19")
    VALUE_05_19 = XmlPeriod("--05-19")
    VALUE_11_08 = XmlPeriod("--11-08")
    VALUE_09_16 = XmlPeriod("--09-16")
    VALUE_05_29 = XmlPeriod("--05-29")
    VALUE_11_18 = XmlPeriod("--11-18")
    VALUE_07_05 = XmlPeriod("--07-05")


@dataclass
class NistschemaSvIvAtomicGMonthDayEnumeration1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gMonthDay-enumeration-1"
        namespace = "NISTSchema-SV-IV-atomic-gMonthDay-enumeration-1-NS"

    value: Optional[NistschemaSvIvAtomicGMonthDayEnumeration1Type] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
