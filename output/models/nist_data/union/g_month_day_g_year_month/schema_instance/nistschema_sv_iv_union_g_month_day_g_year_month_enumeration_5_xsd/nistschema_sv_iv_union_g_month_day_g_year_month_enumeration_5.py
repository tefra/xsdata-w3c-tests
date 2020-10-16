from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-union-gMonthDay-gYearMonth-enumeration-5-NS"


class NistschemaSvIvUnionGMonthDayGYearMonthEnumeration5Type(Enum):
    """
    :cvar VALUE_05_07:
    :cvar VALUE_07_18:
    :cvar VALUE_2011_09:
    :cvar VALUE_2019_10:
    :cvar VALUE_03_13:
    :cvar VALUE_02_15:
    :cvar VALUE_11_30:
    :cvar VALUE_1997_02:
    """
    VALUE_05_07 = "--05-07"
    VALUE_07_18 = "--07-18"
    VALUE_2011_09 = "2011-09"
    VALUE_2019_10 = "2019-10"
    VALUE_03_13 = "--03-13"
    VALUE_02_15 = "--02-15"
    VALUE_11_30 = "--11-30"
    VALUE_1997_02 = "1997-02"


@dataclass
class NistschemaSvIvUnionGMonthDayGYearMonthEnumeration5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-union-gMonthDay-gYearMonth-enumeration-5"
        namespace = "NISTSchema-SV-IV-union-gMonthDay-gYearMonth-enumeration-5-NS"

    value: Optional[NistschemaSvIvUnionGMonthDayGYearMonthEnumeration5Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
