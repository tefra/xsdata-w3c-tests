from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-union-gMonthDay-gYearMonth-enumeration-3-NS"


class NistschemaSvIvUnionGMonthDayGYearMonthEnumeration3Type(Enum):
    """
    :cvar VALUE_01_10:
    :cvar VALUE_06_07:
    :cvar VALUE_08_04:
    :cvar VALUE_11_25:
    :cvar VALUE_1980_06:
    :cvar VALUE_1990_11:
    :cvar VALUE_2011_09:
    :cvar VALUE_2015_07:
    :cvar VALUE_2020_12:
    """
    VALUE_01_10 = "--01-10"
    VALUE_06_07 = "--06-07"
    VALUE_08_04 = "--08-04"
    VALUE_11_25 = "--11-25"
    VALUE_1980_06 = "1980-06"
    VALUE_1990_11 = "1990-11"
    VALUE_2011_09 = "2011-09"
    VALUE_2015_07 = "2015-07"
    VALUE_2020_12 = "2020-12"


@dataclass
class NistschemaSvIvUnionGMonthDayGYearMonthEnumeration3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-union-gMonthDay-gYearMonth-enumeration-3"
        namespace = "NISTSchema-SV-IV-union-gMonthDay-gYearMonth-enumeration-3-NS"

    value: Optional[NistschemaSvIvUnionGMonthDayGYearMonthEnumeration3Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
