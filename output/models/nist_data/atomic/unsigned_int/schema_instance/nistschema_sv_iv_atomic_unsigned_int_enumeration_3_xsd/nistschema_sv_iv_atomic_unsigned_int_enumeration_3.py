from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedInt-enumeration-3-NS"


class NistschemaSvIvAtomicUnsignedIntEnumeration3Type(Enum):
    """
    :cvar VALUE_2421249:
    :cvar VALUE_47:
    :cvar VALUE_6248:
    :cvar VALUE_70884037:
    :cvar VALUE_8001:
    :cvar VALUE_90949193:
    :cvar VALUE_9175:
    :cvar VALUE_959:
    """
    VALUE_2421249 = 2421249
    VALUE_47 = 47
    VALUE_6248 = 6248
    VALUE_70884037 = 70884037
    VALUE_8001 = 8001
    VALUE_90949193 = 90949193
    VALUE_9175 = 9175
    VALUE_959 = 959


@dataclass
class NistschemaSvIvAtomicUnsignedIntEnumeration3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedInt-enumeration-3"
        namespace = "NISTSchema-SV-IV-atomic-unsignedInt-enumeration-3-NS"

    value: Optional[NistschemaSvIvAtomicUnsignedIntEnumeration3Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
