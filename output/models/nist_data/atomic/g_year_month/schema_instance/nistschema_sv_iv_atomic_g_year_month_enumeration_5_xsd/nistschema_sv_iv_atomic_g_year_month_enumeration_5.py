from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYearMonth-enumeration-5-NS"


class NistschemaSvIvAtomicGYearMonthEnumeration5Type(Enum):
    VALUE_2020_08 = XmlPeriod("2020-08")
    VALUE_2027_03 = XmlPeriod("2027-03")
    VALUE_1991_12 = XmlPeriod("1991-12")
    VALUE_1978_06 = XmlPeriod("1978-06")
    VALUE_1992_07 = XmlPeriod("1992-07")
    VALUE_1998_08 = XmlPeriod("1998-08")
    VALUE_2027_02 = XmlPeriod("2027-02")
    VALUE_2013_02 = XmlPeriod("2013-02")


@dataclass
class NistschemaSvIvAtomicGYearMonthEnumeration5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYearMonth-enumeration-5"
        namespace = "NISTSchema-SV-IV-atomic-gYearMonth-enumeration-5-NS"

    value: Optional[NistschemaSvIvAtomicGYearMonthEnumeration5Type] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
