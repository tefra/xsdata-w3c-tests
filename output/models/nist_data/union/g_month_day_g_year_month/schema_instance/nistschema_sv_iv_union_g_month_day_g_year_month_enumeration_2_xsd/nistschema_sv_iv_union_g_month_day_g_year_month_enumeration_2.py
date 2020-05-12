from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-union-gMonthDay-gYearMonth-enumeration-2-NS"


class NistschemaSvIvUnionGMonthDayGYearMonthEnumeration2Type(Enum):
    """
    :cvar VALUE_05_21:
    :cvar VALUE_2005_08:
    :cvar VALUE_10_17:
    :cvar VALUE_1995_07:
    :cvar VALUE_1984_12:
    :cvar VALUE_06_14:
    :cvar VALUE_1994_09:
    :cvar VALUE_1980_05:
    """
    VALUE_05_21 = "--05-21"
    VALUE_2005_08 = "2005-08"
    VALUE_10_17 = "--10-17"
    VALUE_1995_07 = "1995-07"
    VALUE_1984_12 = "1984-12"
    VALUE_06_14 = "--06-14"
    VALUE_1994_09 = "1994-09"
    VALUE_1980_05 = "1980-05"


@dataclass
class NistschemaSvIvUnionGMonthDayGYearMonthEnumeration2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-union-gMonthDay-gYearMonth-enumeration-2"
        namespace = "NISTSchema-SV-IV-union-gMonthDay-gYearMonth-enumeration-2-NS"

    value: Optional[NistschemaSvIvUnionGMonthDayGYearMonthEnumeration2Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
