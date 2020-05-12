from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-short-enumeration-2-NS"


class NistschemaSvIvAtomicShortEnumeration2Type(Enum):
    """
    :cvar VALUE_154:
    :cvar VALUE_3:
    :cvar VALUE_4:
    :cvar VALUE_589:
    :cvar VALUE_78:
    :cvar VALUE_MINUS_32768:
    :cvar VALUE_MINUS_7086:
    :cvar VALUE_MINUS_888:
    """
    VALUE_154 = 154
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_589 = 589
    VALUE_78 = 78
    VALUE_MINUS_32768 = -32768
    VALUE_MINUS_7086 = -7086
    VALUE_MINUS_888 = -888


@dataclass
class NistschemaSvIvAtomicShortEnumeration2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-short-enumeration-2"
        namespace = "NISTSchema-SV-IV-atomic-short-enumeration-2-NS"

    value: Optional[NistschemaSvIvAtomicShortEnumeration2Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
