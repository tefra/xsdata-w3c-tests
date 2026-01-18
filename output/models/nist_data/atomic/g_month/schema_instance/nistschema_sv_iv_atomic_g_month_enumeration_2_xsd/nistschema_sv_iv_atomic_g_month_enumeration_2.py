from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gMonth-enumeration-2-NS"


class NistschemaSvIvAtomicGMonthEnumeration2Type(Enum):
    VALUE_02 = XmlPeriod("--02")
    VALUE_12 = XmlPeriod("--12")
    VALUE_06 = XmlPeriod("--06")
    VALUE_04 = XmlPeriod("--04")
    VALUE_11 = XmlPeriod("--11")


@dataclass(kw_only=True)
class NistschemaSvIvAtomicGMonthEnumeration2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gMonth-enumeration-2"
        namespace = "NISTSchema-SV-IV-atomic-gMonth-enumeration-2-NS"

    value: NistschemaSvIvAtomicGMonthEnumeration2Type = field(
        metadata={
            "required": True,
        }
    )
