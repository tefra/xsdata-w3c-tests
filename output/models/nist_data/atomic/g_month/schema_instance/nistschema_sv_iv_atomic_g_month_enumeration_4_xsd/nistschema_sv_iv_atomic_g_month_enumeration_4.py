from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gMonth-enumeration-4-NS"


class NistschemaSvIvAtomicGMonthEnumeration4Type(Enum):
    VALUE_07 = XmlPeriod("--07")
    VALUE_03 = XmlPeriod("--03")
    VALUE_05 = XmlPeriod("--05")
    VALUE_02 = XmlPeriod("--02")
    VALUE_10 = XmlPeriod("--10")
    VALUE_04 = XmlPeriod("--04")


@dataclass
class NistschemaSvIvAtomicGMonthEnumeration4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gMonth-enumeration-4"
        namespace = "NISTSchema-SV-IV-atomic-gMonth-enumeration-4-NS"

    value: Optional[NistschemaSvIvAtomicGMonthEnumeration4Type] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
