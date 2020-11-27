from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYearMonth-enumeration-2-NS"


class NistschemaSvIvAtomicGYearMonthEnumeration2Type(Enum):
    VALUE_2017_08 = "2017-08"
    VALUE_1986_04 = "1986-04"
    VALUE_2000_01 = "2000-01"
    VALUE_2015_06 = "2015-06"
    VALUE_2010_09 = "2010-09"
    VALUE_2002_07 = "2002-07"
    VALUE_2020_10 = "2020-10"
    VALUE_2012_02 = "2012-02"


@dataclass
class NistschemaSvIvAtomicGYearMonthEnumeration2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYearMonth-enumeration-2"
        namespace = "NISTSchema-SV-IV-atomic-gYearMonth-enumeration-2-NS"

    value: Optional[NistschemaSvIvAtomicGYearMonthEnumeration2Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
