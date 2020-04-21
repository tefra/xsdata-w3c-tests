from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedShort-enumeration-3-NS"


class NistschemaSvIvAtomicUnsignedShortEnumeration3Type(Enum):
    """
    :cvar VALUE_12:
    :cvar VALUE_1963:
    :cvar VALUE_2521:
    :cvar VALUE_3449:
    :cvar VALUE_4:
    :cvar VALUE_58929:
    :cvar VALUE_609:
    :cvar VALUE_6997:
    """
    VALUE_12 = 12
    VALUE_1963 = 1963
    VALUE_2521 = 2521
    VALUE_3449 = 3449
    VALUE_4 = 4
    VALUE_58929 = 58929
    VALUE_609 = 609
    VALUE_6997 = 6997


@dataclass
class NistschemaSvIvAtomicUnsignedShortEnumeration3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedShort-enumeration-3"
        namespace = "NISTSchema-SV-IV-atomic-unsignedShort-enumeration-3-NS"

    value: Optional[NistschemaSvIvAtomicUnsignedShortEnumeration3Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
