from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedLong-enumeration-3-NS"


class NistschemaSvIvAtomicUnsignedLongEnumeration3Type(Enum):
    """
    :cvar VALUE_33505897371058979:
    :cvar VALUE_38:
    :cvar VALUE_48185:
    :cvar VALUE_492728752144644066:
    :cvar VALUE_51135955:
    :cvar VALUE_5876730603:
    :cvar VALUE_7037409938820924:
    :cvar VALUE_760056434:
    """
    VALUE_33505897371058979 = 33505897371058979
    VALUE_38 = 38
    VALUE_48185 = 48185
    VALUE_492728752144644066 = 492728752144644066
    VALUE_51135955 = 51135955
    VALUE_5876730603 = 5876730603
    VALUE_7037409938820924 = 7037409938820924
    VALUE_760056434 = 760056434


@dataclass
class NistschemaSvIvAtomicUnsignedLongEnumeration3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedLong-enumeration-3"
        namespace = "NISTSchema-SV-IV-atomic-unsignedLong-enumeration-3-NS"

    value: Optional[NistschemaSvIvAtomicUnsignedLongEnumeration3Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
