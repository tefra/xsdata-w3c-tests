from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gMonthDay-enumeration-2-NS"


class NistschemaSvIvAtomicGMonthDayEnumeration2Type(Enum):
    """
    :cvar VALUE_09_24:
    :cvar VALUE_01_28:
    :cvar VALUE_08_31:
    :cvar VALUE_08_20:
    :cvar VALUE_12_06:
    """
    VALUE_09_24 = "--09-24"
    VALUE_01_28 = "--01-28"
    VALUE_08_31 = "--08-31"
    VALUE_08_20 = "--08-20"
    VALUE_12_06 = "--12-06"


@dataclass
class NistschemaSvIvAtomicGMonthDayEnumeration2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gMonthDay-enumeration-2"
        namespace = "NISTSchema-SV-IV-atomic-gMonthDay-enumeration-2-NS"

    value: Optional[NistschemaSvIvAtomicGMonthDayEnumeration2Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
