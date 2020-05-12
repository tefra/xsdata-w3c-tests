from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedInt-enumeration-2-NS"


class NistschemaSvIvAtomicUnsignedIntEnumeration2Type(Enum):
    """
    :cvar VALUE_1331474827:
    :cvar VALUE_25:
    :cvar VALUE_576176:
    :cvar VALUE_944130:
    :cvar VALUE_62:
    :cvar VALUE_46:
    :cvar VALUE_5135198:
    :cvar VALUE_2157977:
    :cvar VALUE_311:
    """
    VALUE_1331474827 = 1331474827
    VALUE_25 = 25
    VALUE_576176 = 576176
    VALUE_944130 = 944130
    VALUE_62 = 62
    VALUE_46 = 46
    VALUE_5135198 = 5135198
    VALUE_2157977 = 2157977
    VALUE_311 = 311


@dataclass
class NistschemaSvIvAtomicUnsignedIntEnumeration2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedInt-enumeration-2"
        namespace = "NISTSchema-SV-IV-atomic-unsignedInt-enumeration-2-NS"

    value: Optional[NistschemaSvIvAtomicUnsignedIntEnumeration2Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
