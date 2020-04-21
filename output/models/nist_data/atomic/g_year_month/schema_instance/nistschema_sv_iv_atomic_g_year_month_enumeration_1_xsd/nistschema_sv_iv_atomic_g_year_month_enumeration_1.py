from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYearMonth-enumeration-1-NS"


class NistschemaSvIvAtomicGYearMonthEnumeration1Type(Enum):
    """
    :cvar VALUE_1980_03:
    :cvar VALUE_2014_08:
    :cvar VALUE_2017_03:
    :cvar VALUE_2017_10:
    :cvar VALUE_2028_04:
    """
    VALUE_1980_03 = "1980-03"
    VALUE_2014_08 = "2014-08"
    VALUE_2017_03 = "2017-03"
    VALUE_2017_10 = "2017-10"
    VALUE_2028_04 = "2028-04"


@dataclass
class NistschemaSvIvAtomicGYearMonthEnumeration1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYearMonth-enumeration-1"
        namespace = "NISTSchema-SV-IV-atomic-gYearMonth-enumeration-1-NS"

    value: Optional[NistschemaSvIvAtomicGYearMonthEnumeration1Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
