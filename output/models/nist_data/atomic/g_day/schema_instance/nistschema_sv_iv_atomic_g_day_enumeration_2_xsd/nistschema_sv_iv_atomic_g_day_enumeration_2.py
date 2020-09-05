from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gDay-enumeration-2-NS"


class NistschemaSvIvAtomicGDayEnumeration2Type(Enum):
    """
    :cvar VALUE_04:
    :cvar VALUE_22:
    :cvar VALUE_20:
    :cvar VALUE_18:
    :cvar VALUE_12:
    :cvar VALUE_10:
    :cvar VALUE_08:
    """
    VALUE_04 = "---04"
    VALUE_22 = "---22"
    VALUE_20 = "---20"
    VALUE_18 = "---18"
    VALUE_12 = "---12"
    VALUE_10 = "---10"
    VALUE_08 = "---08"


@dataclass
class NistschemaSvIvAtomicGDayEnumeration2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gDay-enumeration-2"
        namespace = "NISTSchema-SV-IV-atomic-gDay-enumeration-2-NS"

    value: Optional[NistschemaSvIvAtomicGDayEnumeration2Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
