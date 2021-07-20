from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gMonthDay-enumeration-5-NS"


class NistschemaSvIvAtomicGMonthDayEnumeration5Type(Enum):
    VALUE_05_21 = XmlPeriod("--05-21")
    VALUE_09_18 = XmlPeriod("--09-18")
    VALUE_03_28 = XmlPeriod("--03-28")
    VALUE_04_03 = XmlPeriod("--04-03")
    VALUE_09_13 = XmlPeriod("--09-13")
    VALUE_08_07 = XmlPeriod("--08-07")
    VALUE_07_11 = XmlPeriod("--07-11")
    VALUE_09_03 = XmlPeriod("--09-03")
    VALUE_02_23 = XmlPeriod("--02-23")


@dataclass
class NistschemaSvIvAtomicGMonthDayEnumeration5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gMonthDay-enumeration-5"
        namespace = "NISTSchema-SV-IV-atomic-gMonthDay-enumeration-5-NS"

    value: Optional[NistschemaSvIvAtomicGMonthDayEnumeration5Type] = field(
        default=None
    )
