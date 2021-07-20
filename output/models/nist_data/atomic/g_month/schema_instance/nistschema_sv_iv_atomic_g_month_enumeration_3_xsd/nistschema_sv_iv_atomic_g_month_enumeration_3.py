from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gMonth-enumeration-3-NS"


class NistschemaSvIvAtomicGMonthEnumeration3Type(Enum):
    VALUE_02 = XmlPeriod("--02")
    VALUE_12 = XmlPeriod("--12")
    VALUE_03 = XmlPeriod("--03")
    VALUE_04 = XmlPeriod("--04")
    VALUE_11 = XmlPeriod("--11")


@dataclass
class NistschemaSvIvAtomicGMonthEnumeration3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gMonth-enumeration-3"
        namespace = "NISTSchema-SV-IV-atomic-gMonth-enumeration-3-NS"

    value: Optional[NistschemaSvIvAtomicGMonthEnumeration3Type] = field(
        default=None
    )
