from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gMonth-enumeration-4-NS"


class NistschemaSvIvAtomicGMonthEnumeration4Type(Enum):
    """
    :cvar VALUE_02:
    :cvar VALUE_03:
    :cvar VALUE_04:
    :cvar VALUE_05:
    :cvar VALUE_07:
    :cvar VALUE_10:
    """
    VALUE_02 = "--02"
    VALUE_03 = "--03"
    VALUE_04 = "--04"
    VALUE_05 = "--05"
    VALUE_07 = "--07"
    VALUE_10 = "--10"


@dataclass
class NistschemaSvIvAtomicGMonthEnumeration4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gMonth-enumeration-4"
        namespace = "NISTSchema-SV-IV-atomic-gMonth-enumeration-4-NS"

    value: Optional[NistschemaSvIvAtomicGMonthEnumeration4Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
