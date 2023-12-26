from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYear-enumeration-3-NS"


class NistschemaSvIvAtomicGYearEnumeration3Type(Enum):
    VALUE_2004 = XmlPeriod("2004")
    VALUE_2014 = XmlPeriod("2014")
    VALUE_1991 = XmlPeriod("1991")
    VALUE_2001 = XmlPeriod("2001")
    VALUE_2021 = XmlPeriod("2021")


@dataclass
class NistschemaSvIvAtomicGYearEnumeration3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYear-enumeration-3"
        namespace = "NISTSchema-SV-IV-atomic-gYear-enumeration-3-NS"

    value: Optional[NistschemaSvIvAtomicGYearEnumeration3Type] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
