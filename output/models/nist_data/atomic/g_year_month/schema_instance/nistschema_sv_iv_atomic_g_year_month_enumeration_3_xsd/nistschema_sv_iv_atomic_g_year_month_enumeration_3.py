from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYearMonth-enumeration-3-NS"


class NistschemaSvIvAtomicGYearMonthEnumeration3Type(Enum):
    """
    :cvar VALUE_1978_12:
    :cvar VALUE_2002_12:
    :cvar VALUE_2001_09:
    :cvar VALUE_1972_08:
    :cvar VALUE_1973_09:
    """
    VALUE_1978_12 = "1978-12"
    VALUE_2002_12 = "2002-12"
    VALUE_2001_09 = "2001-09"
    VALUE_1972_08 = "1972-08"
    VALUE_1973_09 = "1973-09"


@dataclass
class NistschemaSvIvAtomicGYearMonthEnumeration3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYearMonth-enumeration-3"
        namespace = "NISTSchema-SV-IV-atomic-gYearMonth-enumeration-3-NS"

    value: Optional[NistschemaSvIvAtomicGYearMonthEnumeration3Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
