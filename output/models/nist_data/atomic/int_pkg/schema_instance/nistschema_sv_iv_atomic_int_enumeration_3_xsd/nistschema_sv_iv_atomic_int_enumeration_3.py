from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-int-enumeration-3-NS"


class NistschemaSvIvAtomicIntEnumeration3Type(Enum):
    """
    :cvar VALUE_MINUS_2142090:
    :cvar VALUE_MINUS_314:
    :cvar VALUE_MINUS_53685045:
    :cvar VALUE_2147483647:
    :cvar VALUE_323669986:
    :cvar VALUE_43292492:
    :cvar VALUE_70977758:
    :cvar VALUE_9391921:
    """
    VALUE_MINUS_2142090 = -2142090
    VALUE_MINUS_314 = -314
    VALUE_MINUS_53685045 = -53685045
    VALUE_2147483647 = 2147483647
    VALUE_323669986 = 323669986
    VALUE_43292492 = 43292492
    VALUE_70977758 = 70977758
    VALUE_9391921 = 9391921


@dataclass
class NistschemaSvIvAtomicIntEnumeration3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-int-enumeration-3"
        namespace = "NISTSchema-SV-IV-atomic-int-enumeration-3-NS"

    value: Optional[NistschemaSvIvAtomicIntEnumeration3Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )