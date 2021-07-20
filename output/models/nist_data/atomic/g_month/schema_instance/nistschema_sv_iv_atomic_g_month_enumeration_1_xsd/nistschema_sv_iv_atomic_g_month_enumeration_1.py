from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gMonth-enumeration-1-NS"


class NistschemaSvIvAtomicGMonthEnumeration1Type(Enum):
    VALUE_01 = XmlPeriod("--01")
    VALUE_08 = XmlPeriod("--08")
    VALUE_02 = XmlPeriod("--02")
    VALUE_05 = XmlPeriod("--05")
    VALUE_04 = XmlPeriod("--04")


@dataclass
class NistschemaSvIvAtomicGMonthEnumeration1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gMonth-enumeration-1"
        namespace = "NISTSchema-SV-IV-atomic-gMonth-enumeration-1-NS"

    value: Optional[NistschemaSvIvAtomicGMonthEnumeration1Type] = field(
        default=None
    )
