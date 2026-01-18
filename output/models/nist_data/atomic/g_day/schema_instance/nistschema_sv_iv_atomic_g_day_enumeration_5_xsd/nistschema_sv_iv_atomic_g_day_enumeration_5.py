from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gDay-enumeration-5-NS"


class NistschemaSvIvAtomicGDayEnumeration5Type(Enum):
    VALUE_21 = XmlPeriod("---21")
    VALUE_23 = XmlPeriod("---23")
    VALUE_13 = XmlPeriod("---13")
    VALUE_26 = XmlPeriod("---26")
    VALUE_24 = XmlPeriod("---24")
    VALUE_18 = XmlPeriod("---18")
    VALUE_30 = XmlPeriod("---30")
    VALUE_14 = XmlPeriod("---14")


@dataclass(kw_only=True)
class NistschemaSvIvAtomicGDayEnumeration5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gDay-enumeration-5"
        namespace = "NISTSchema-SV-IV-atomic-gDay-enumeration-5-NS"

    value: NistschemaSvIvAtomicGDayEnumeration5Type = field(
        metadata={
            "required": True,
        }
    )
