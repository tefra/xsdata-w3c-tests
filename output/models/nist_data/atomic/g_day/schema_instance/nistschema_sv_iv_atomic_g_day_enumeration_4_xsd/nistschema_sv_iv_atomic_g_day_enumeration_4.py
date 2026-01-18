from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gDay-enumeration-4-NS"


class NistschemaSvIvAtomicGDayEnumeration4Type(Enum):
    VALUE_15 = XmlPeriod("---15")
    VALUE_05 = XmlPeriod("---05")
    VALUE_17 = XmlPeriod("---17")
    VALUE_12 = XmlPeriod("---12")
    VALUE_21 = XmlPeriod("---21")
    VALUE_18 = XmlPeriod("---18")


@dataclass(kw_only=True)
class NistschemaSvIvAtomicGDayEnumeration4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gDay-enumeration-4"
        namespace = "NISTSchema-SV-IV-atomic-gDay-enumeration-4-NS"

    value: NistschemaSvIvAtomicGDayEnumeration4Type = field(
        metadata={
            "required": True,
        }
    )
