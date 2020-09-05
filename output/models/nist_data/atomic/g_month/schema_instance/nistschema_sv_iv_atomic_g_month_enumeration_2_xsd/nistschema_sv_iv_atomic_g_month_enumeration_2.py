from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gMonth-enumeration-2-NS"


class NistschemaSvIvAtomicGMonthEnumeration2Type(Enum):
    """
    :cvar VALUE_02:
    :cvar VALUE_12:
    :cvar VALUE_06:
    :cvar VALUE_04:
    :cvar VALUE_11:
    """
    VALUE_02 = "--02"
    VALUE_12 = "--12"
    VALUE_06 = "--06"
    VALUE_04 = "--04"
    VALUE_11 = "--11"


@dataclass
class NistschemaSvIvAtomicGMonthEnumeration2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gMonth-enumeration-2"
        namespace = "NISTSchema-SV-IV-atomic-gMonth-enumeration-2-NS"

    value: Optional[NistschemaSvIvAtomicGMonthEnumeration2Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
