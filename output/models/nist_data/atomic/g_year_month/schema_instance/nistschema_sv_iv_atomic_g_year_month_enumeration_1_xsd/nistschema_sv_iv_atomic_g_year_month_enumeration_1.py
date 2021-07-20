from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYearMonth-enumeration-1-NS"


class NistschemaSvIvAtomicGYearMonthEnumeration1Type(Enum):
    VALUE_2017_03 = XmlPeriod("2017-03")
    VALUE_2028_04 = XmlPeriod("2028-04")
    VALUE_1980_03 = XmlPeriod("1980-03")
    VALUE_2014_08 = XmlPeriod("2014-08")
    VALUE_2017_10 = XmlPeriod("2017-10")


@dataclass
class NistschemaSvIvAtomicGYearMonthEnumeration1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYearMonth-enumeration-1"
        namespace = "NISTSchema-SV-IV-atomic-gYearMonth-enumeration-1-NS"

    value: Optional[NistschemaSvIvAtomicGYearMonthEnumeration1Type] = field(
        default=None
    )
