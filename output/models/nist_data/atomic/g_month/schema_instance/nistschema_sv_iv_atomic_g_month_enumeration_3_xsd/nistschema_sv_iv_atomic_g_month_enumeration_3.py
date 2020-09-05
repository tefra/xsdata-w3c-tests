from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gMonth-enumeration-3-NS"


class NistschemaSvIvAtomicGMonthEnumeration3Type(Enum):
    """
    :cvar VALUE_02:
    :cvar VALUE_12:
    :cvar VALUE_03:
    :cvar VALUE_04:
    :cvar VALUE_11:
    """
    VALUE_02 = "--02"
    VALUE_12 = "--12"
    VALUE_03 = "--03"
    VALUE_04 = "--04"
    VALUE_11 = "--11"


@dataclass
class NistschemaSvIvAtomicGMonthEnumeration3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gMonth-enumeration-3"
        namespace = "NISTSchema-SV-IV-atomic-gMonth-enumeration-3-NS"

    value: Optional[NistschemaSvIvAtomicGMonthEnumeration3Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
