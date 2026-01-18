from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gDay-enumeration-2-NS"


class NistschemaSvIvAtomicGDayEnumeration2Type(Enum):
    VALUE_04 = XmlPeriod("---04")
    VALUE_22 = XmlPeriod("---22")
    VALUE_20 = XmlPeriod("---20")
    VALUE_18 = XmlPeriod("---18")
    VALUE_12 = XmlPeriod("---12")
    VALUE_10 = XmlPeriod("---10")
    VALUE_08 = XmlPeriod("---08")


@dataclass(kw_only=True)
class NistschemaSvIvAtomicGDayEnumeration2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gDay-enumeration-2"
        namespace = "NISTSchema-SV-IV-atomic-gDay-enumeration-2-NS"

    value: NistschemaSvIvAtomicGDayEnumeration2Type = field(
        metadata={
            "required": True,
        }
    )
