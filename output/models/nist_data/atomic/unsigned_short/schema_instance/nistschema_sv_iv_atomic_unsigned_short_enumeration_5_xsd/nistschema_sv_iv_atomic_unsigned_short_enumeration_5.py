from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedShort-enumeration-5-NS"


class NistschemaSvIvAtomicUnsignedShortEnumeration5Type(Enum):
    """
    :cvar VALUE_3386:
    :cvar VALUE_700:
    :cvar VALUE_1:
    :cvar VALUE_2341:
    :cvar VALUE_65535:
    :cvar VALUE_88:
    :cvar VALUE_3784:
    :cvar VALUE_870:
    """
    VALUE_3386 = 3386
    VALUE_700 = 700
    VALUE_1 = 1
    VALUE_2341 = 2341
    VALUE_65535 = 65535
    VALUE_88 = 88
    VALUE_3784 = 3784
    VALUE_870 = 870


@dataclass
class NistschemaSvIvAtomicUnsignedShortEnumeration5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedShort-enumeration-5"
        namespace = "NISTSchema-SV-IV-atomic-unsignedShort-enumeration-5-NS"

    value: Optional[NistschemaSvIvAtomicUnsignedShortEnumeration5Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
