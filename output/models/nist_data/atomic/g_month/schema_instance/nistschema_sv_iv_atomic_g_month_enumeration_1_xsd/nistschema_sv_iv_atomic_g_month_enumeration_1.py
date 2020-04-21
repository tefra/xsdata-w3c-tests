from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gMonth-enumeration-1-NS"


class NistschemaSvIvAtomicGMonthEnumeration1Type(Enum):
    """
    :cvar VALUE_01:
    :cvar VALUE_02:
    :cvar VALUE_04:
    :cvar VALUE_05:
    :cvar VALUE_08:
    """
    VALUE_01 = "--01"
    VALUE_02 = "--02"
    VALUE_04 = "--04"
    VALUE_05 = "--05"
    VALUE_08 = "--08"


@dataclass
class NistschemaSvIvAtomicGMonthEnumeration1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gMonth-enumeration-1"
        namespace = "NISTSchema-SV-IV-atomic-gMonth-enumeration-1-NS"

    value: Optional[NistschemaSvIvAtomicGMonthEnumeration1Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
