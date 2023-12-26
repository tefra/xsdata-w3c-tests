from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gDay-enumeration-4-NS"


class NistschemaSvIvAtomicGDayEnumeration4Type(Enum):
    VALUE_15 = XmlPeriod("---15")
    VALUE_05 = XmlPeriod("---05")
    VALUE_17 = XmlPeriod("---17")
    VALUE_12 = XmlPeriod("---12")
    VALUE_21 = XmlPeriod("---21")
    VALUE_18 = XmlPeriod("---18")


@dataclass
class NistschemaSvIvAtomicGDayEnumeration4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gDay-enumeration-4"
        namespace = "NISTSchema-SV-IV-atomic-gDay-enumeration-4-NS"

    value: Optional[NistschemaSvIvAtomicGDayEnumeration4Type] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
