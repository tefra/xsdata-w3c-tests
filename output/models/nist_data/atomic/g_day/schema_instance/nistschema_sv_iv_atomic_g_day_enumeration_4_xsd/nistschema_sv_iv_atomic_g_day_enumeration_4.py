from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gDay-enumeration-4-NS"


class NistschemaSvIvAtomicGDayEnumeration4Type(Enum):
    """
    :cvar VALUE_05:
    :cvar VALUE_12:
    :cvar VALUE_15:
    :cvar VALUE_17:
    :cvar VALUE_18:
    :cvar VALUE_21:
    """
    VALUE_05 = "---05"
    VALUE_12 = "---12"
    VALUE_15 = "---15"
    VALUE_17 = "---17"
    VALUE_18 = "---18"
    VALUE_21 = "---21"


@dataclass
class NistschemaSvIvAtomicGDayEnumeration4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gDay-enumeration-4"
        namespace = "NISTSchema-SV-IV-atomic-gDay-enumeration-4-NS"

    value: Optional[NistschemaSvIvAtomicGDayEnumeration4Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
