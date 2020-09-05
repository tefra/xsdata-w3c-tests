from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-union-gMonthDay-gYearMonth-enumeration-1-NS"


class NistschemaSvIvUnionGMonthDayGYearMonthEnumeration1Type(Enum):
    """
    :cvar VALUE_04_23:
    :cvar VALUE_1989_09:
    :cvar VALUE_2015_07:
    :cvar VALUE_11_30:
    :cvar VALUE_2003_07:
    :cvar VALUE_1994_09:
    :cvar VALUE_2023_02:
    :cvar VALUE_1982_09:
    """
    VALUE_04_23 = "--04-23"
    VALUE_1989_09 = "1989-09"
    VALUE_2015_07 = "2015-07"
    VALUE_11_30 = "--11-30"
    VALUE_2003_07 = "2003-07"
    VALUE_1994_09 = "1994-09"
    VALUE_2023_02 = "2023-02"
    VALUE_1982_09 = "1982-09"


@dataclass
class NistschemaSvIvUnionGMonthDayGYearMonthEnumeration1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-union-gMonthDay-gYearMonth-enumeration-1"
        namespace = "NISTSchema-SV-IV-union-gMonthDay-gYearMonth-enumeration-1-NS"

    value: Optional[NistschemaSvIvUnionGMonthDayGYearMonthEnumeration1Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
