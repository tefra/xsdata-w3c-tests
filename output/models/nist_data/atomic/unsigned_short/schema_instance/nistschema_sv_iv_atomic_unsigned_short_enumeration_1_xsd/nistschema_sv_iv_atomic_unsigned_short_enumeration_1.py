from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedShort-enumeration-1-NS"


class NistschemaSvIvAtomicUnsignedShortEnumeration1Type(Enum):
    """
    :cvar VALUE_121:
    :cvar VALUE_272:
    :cvar VALUE_28:
    :cvar VALUE_357:
    :cvar VALUE_51760:
    :cvar VALUE_570:
    :cvar VALUE_603:
    :cvar VALUE_65535:
    """
    VALUE_121 = 121
    VALUE_272 = 272
    VALUE_28 = 28
    VALUE_357 = 357
    VALUE_51760 = 51760
    VALUE_570 = 570
    VALUE_603 = 603
    VALUE_65535 = 65535


@dataclass
class NistschemaSvIvAtomicUnsignedShortEnumeration1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedShort-enumeration-1"
        namespace = "NISTSchema-SV-IV-atomic-unsignedShort-enumeration-1-NS"

    value: Optional[NistschemaSvIvAtomicUnsignedShortEnumeration1Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
