from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gDay-enumeration-1-NS"


class NistschemaSvIvAtomicGDayEnumeration1Type(Enum):
    """
    :cvar VALUE_15:
    :cvar VALUE_29:
    :cvar VALUE_30:
    :cvar VALUE_26:
    :cvar VALUE_16:
    :cvar VALUE_08:
    :cvar VALUE_18:
    :cvar VALUE_07:
    """
    VALUE_15 = "---15"
    VALUE_29 = "---29"
    VALUE_30 = "---30"
    VALUE_26 = "---26"
    VALUE_16 = "---16"
    VALUE_08 = "---08"
    VALUE_18 = "---18"
    VALUE_07 = "---07"


@dataclass
class NistschemaSvIvAtomicGDayEnumeration1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gDay-enumeration-1"
        namespace = "NISTSchema-SV-IV-atomic-gDay-enumeration-1-NS"

    value: Optional[NistschemaSvIvAtomicGDayEnumeration1Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
