from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYearMonth-enumeration-5-NS"


class NistschemaSvIvAtomicGYearMonthEnumeration5Type(Enum):
    """
    :cvar VALUE_2020_08:
    :cvar VALUE_2027_03:
    :cvar VALUE_1991_12:
    :cvar VALUE_1978_06:
    :cvar VALUE_1992_07:
    :cvar VALUE_1998_08:
    :cvar VALUE_2027_02:
    :cvar VALUE_2013_02:
    """
    VALUE_2020_08 = "2020-08"
    VALUE_2027_03 = "2027-03"
    VALUE_1991_12 = "1991-12"
    VALUE_1978_06 = "1978-06"
    VALUE_1992_07 = "1992-07"
    VALUE_1998_08 = "1998-08"
    VALUE_2027_02 = "2027-02"
    VALUE_2013_02 = "2013-02"


@dataclass
class NistschemaSvIvAtomicGYearMonthEnumeration5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYearMonth-enumeration-5"
        namespace = "NISTSchema-SV-IV-atomic-gYearMonth-enumeration-5-NS"

    value: Optional[NistschemaSvIvAtomicGYearMonthEnumeration5Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
