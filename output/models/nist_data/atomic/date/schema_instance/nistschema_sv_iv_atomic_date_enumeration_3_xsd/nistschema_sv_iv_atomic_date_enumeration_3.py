from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-date-enumeration-3-NS"


class NistschemaSvIvAtomicDateEnumeration3Type(Enum):
    """
    :cvar VALUE_2005_06_19:
    :cvar VALUE_1973_10_26:
    :cvar VALUE_1992_08_14:
    :cvar VALUE_1973_09_16:
    :cvar VALUE_1990_04_07:
    :cvar VALUE_1995_07_16:
    :cvar VALUE_1985_09_24:
    """
    VALUE_2005_06_19 = "2005-06-19"
    VALUE_1973_10_26 = "1973-10-26"
    VALUE_1992_08_14 = "1992-08-14"
    VALUE_1973_09_16 = "1973-09-16"
    VALUE_1990_04_07 = "1990-04-07"
    VALUE_1995_07_16 = "1995-07-16"
    VALUE_1985_09_24 = "1985-09-24"


@dataclass
class NistschemaSvIvAtomicDateEnumeration3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-date-enumeration-3"
        namespace = "NISTSchema-SV-IV-atomic-date-enumeration-3-NS"

    value: Optional[NistschemaSvIvAtomicDateEnumeration3Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
