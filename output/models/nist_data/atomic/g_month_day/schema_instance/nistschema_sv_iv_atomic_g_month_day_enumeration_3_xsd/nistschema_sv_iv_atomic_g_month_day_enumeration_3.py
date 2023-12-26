from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gMonthDay-enumeration-3-NS"


class NistschemaSvIvAtomicGMonthDayEnumeration3Type(Enum):
    VALUE_12_23 = XmlPeriod("--12-23")
    VALUE_07_11 = XmlPeriod("--07-11")
    VALUE_06_24 = XmlPeriod("--06-24")
    VALUE_10_27 = XmlPeriod("--10-27")
    VALUE_09_07 = XmlPeriod("--09-07")
    VALUE_03_29 = XmlPeriod("--03-29")
    VALUE_12_01 = XmlPeriod("--12-01")
    VALUE_01_29 = XmlPeriod("--01-29")
    VALUE_07_09 = XmlPeriod("--07-09")
    VALUE_10_05 = XmlPeriod("--10-05")


@dataclass
class NistschemaSvIvAtomicGMonthDayEnumeration3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gMonthDay-enumeration-3"
        namespace = "NISTSchema-SV-IV-atomic-gMonthDay-enumeration-3-NS"

    value: Optional[NistschemaSvIvAtomicGMonthDayEnumeration3Type] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
