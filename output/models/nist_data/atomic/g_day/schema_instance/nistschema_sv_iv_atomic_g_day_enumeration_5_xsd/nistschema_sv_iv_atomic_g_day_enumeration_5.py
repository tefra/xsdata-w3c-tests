from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gDay-enumeration-5-NS"


class NistschemaSvIvAtomicGDayEnumeration5Type(Enum):
    """
    :cvar VALUE_13:
    :cvar VALUE_14:
    :cvar VALUE_18:
    :cvar VALUE_21:
    :cvar VALUE_23:
    :cvar VALUE_24:
    :cvar VALUE_26:
    :cvar VALUE_30:
    """
    VALUE_13 = "---13"
    VALUE_14 = "---14"
    VALUE_18 = "---18"
    VALUE_21 = "---21"
    VALUE_23 = "---23"
    VALUE_24 = "---24"
    VALUE_26 = "---26"
    VALUE_30 = "---30"


@dataclass
class NistschemaSvIvAtomicGDayEnumeration5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gDay-enumeration-5"
        namespace = "NISTSchema-SV-IV-atomic-gDay-enumeration-5-NS"

    value: Optional[NistschemaSvIvAtomicGDayEnumeration5Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )