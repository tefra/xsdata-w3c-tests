from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gDay-enumeration-3-NS"


class NistschemaSvIvAtomicGDayEnumeration3Type(Enum):
    VALUE_15 = XmlPeriod("---15")
    VALUE_27 = XmlPeriod("---27")
    VALUE_16 = XmlPeriod("---16")
    VALUE_22 = XmlPeriod("---22")
    VALUE_12 = XmlPeriod("---12")
    VALUE_30 = XmlPeriod("---30")
    VALUE_24 = XmlPeriod("---24")
    VALUE_14 = XmlPeriod("---14")
    VALUE_09 = XmlPeriod("---09")


@dataclass
class NistschemaSvIvAtomicGDayEnumeration3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gDay-enumeration-3"
        namespace = "NISTSchema-SV-IV-atomic-gDay-enumeration-3-NS"

    value: Optional[NistschemaSvIvAtomicGDayEnumeration3Type] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
