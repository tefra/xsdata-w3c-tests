from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYear-enumeration-4-NS"


class NistschemaSvIvAtomicGYearEnumeration4Type(Enum):
    VALUE_1978 = XmlPeriod("1978")
    VALUE_2027 = XmlPeriod("2027")
    VALUE_2007 = XmlPeriod("2007")
    VALUE_1970 = XmlPeriod("1970")
    VALUE_2021 = XmlPeriod("2021")
    VALUE_2016 = XmlPeriod("2016")
    VALUE_2014 = XmlPeriod("2014")
    VALUE_2015 = XmlPeriod("2015")
    VALUE_2023 = XmlPeriod("2023")
    VALUE_2002 = XmlPeriod("2002")


@dataclass
class NistschemaSvIvAtomicGYearEnumeration4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYear-enumeration-4"
        namespace = "NISTSchema-SV-IV-atomic-gYear-enumeration-4-NS"

    value: Optional[NistschemaSvIvAtomicGYearEnumeration4Type] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
