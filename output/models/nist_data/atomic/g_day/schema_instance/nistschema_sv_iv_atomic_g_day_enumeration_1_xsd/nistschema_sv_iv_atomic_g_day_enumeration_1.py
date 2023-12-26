from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gDay-enumeration-1-NS"


class NistschemaSvIvAtomicGDayEnumeration1Type(Enum):
    VALUE_15 = XmlPeriod("---15")
    VALUE_29 = XmlPeriod("---29")
    VALUE_30 = XmlPeriod("---30")
    VALUE_26 = XmlPeriod("---26")
    VALUE_16 = XmlPeriod("---16")
    VALUE_08 = XmlPeriod("---08")
    VALUE_18 = XmlPeriod("---18")
    VALUE_07 = XmlPeriod("---07")


@dataclass
class NistschemaSvIvAtomicGDayEnumeration1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gDay-enumeration-1"
        namespace = "NISTSchema-SV-IV-atomic-gDay-enumeration-1-NS"

    value: Optional[NistschemaSvIvAtomicGDayEnumeration1Type] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
