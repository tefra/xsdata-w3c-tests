from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gMonthDay-enumeration-4-NS"


class NistschemaSvIvAtomicGMonthDayEnumeration4Type(Enum):
    VALUE_06_07 = XmlPeriod("--06-07")
    VALUE_11_20 = XmlPeriod("--11-20")
    VALUE_01_29 = XmlPeriod("--01-29")
    VALUE_11_11 = XmlPeriod("--11-11")
    VALUE_11_17 = XmlPeriod("--11-17")
    VALUE_05_08 = XmlPeriod("--05-08")
    VALUE_07_06 = XmlPeriod("--07-06")
    VALUE_12_01 = XmlPeriod("--12-01")
    VALUE_05_07 = XmlPeriod("--05-07")
    VALUE_09_03 = XmlPeriod("--09-03")


@dataclass(kw_only=True)
class NistschemaSvIvAtomicGMonthDayEnumeration4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gMonthDay-enumeration-4"
        namespace = "NISTSchema-SV-IV-atomic-gMonthDay-enumeration-4-NS"

    value: NistschemaSvIvAtomicGMonthDayEnumeration4Type = field(
        metadata={
            "required": True,
        }
    )
