from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-union-gMonthDay-gYearMonth-enumeration-4-NS"


class NistschemaSvIvUnionGMonthDayGYearMonthEnumeration4Type(Enum):
    """
    :cvar VALUE_1989_06:
    :cvar VALUE_2003_07:
    :cvar VALUE_12_24:
    :cvar VALUE_01_01:
    :cvar VALUE_2005_08:
    :cvar VALUE_04_02:
    :cvar VALUE_11_30:
    :cvar VALUE_2011_09:
    """
    VALUE_1989_06 = "1989-06"
    VALUE_2003_07 = "2003-07"
    VALUE_12_24 = "--12-24"
    VALUE_01_01 = "--01-01"
    VALUE_2005_08 = "2005-08"
    VALUE_04_02 = "--04-02"
    VALUE_11_30 = "--11-30"
    VALUE_2011_09 = "2011-09"


@dataclass
class NistschemaSvIvUnionGMonthDayGYearMonthEnumeration4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-union-gMonthDay-gYearMonth-enumeration-4"
        namespace = "NISTSchema-SV-IV-union-gMonthDay-gYearMonth-enumeration-4-NS"

    value: Optional[NistschemaSvIvUnionGMonthDayGYearMonthEnumeration4Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
