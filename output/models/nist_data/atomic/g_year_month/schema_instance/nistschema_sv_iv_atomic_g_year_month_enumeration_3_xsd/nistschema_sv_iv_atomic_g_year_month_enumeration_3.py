from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xsdata.models.datatype import Period

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYearMonth-enumeration-3-NS"


class NistschemaSvIvAtomicGYearMonthEnumeration3Type(Enum):
    VALUE_1978_12 = Period("1978-12")
    VALUE_2002_12 = Period("2002-12")
    VALUE_2001_09 = Period("2001-09")
    VALUE_1972_08 = Period("1972-08")
    VALUE_1973_09 = Period("1973-09")


@dataclass
class NistschemaSvIvAtomicGYearMonthEnumeration3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYearMonth-enumeration-3"
        namespace = "NISTSchema-SV-IV-atomic-gYearMonth-enumeration-3-NS"

    value: Optional[NistschemaSvIvAtomicGYearMonthEnumeration3Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
