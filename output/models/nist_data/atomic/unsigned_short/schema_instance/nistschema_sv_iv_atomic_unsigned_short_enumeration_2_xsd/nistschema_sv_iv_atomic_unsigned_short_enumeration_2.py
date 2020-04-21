from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedShort-enumeration-2-NS"


class NistschemaSvIvAtomicUnsignedShortEnumeration2Type(Enum):
    """
    :cvar VALUE_296:
    :cvar VALUE_30:
    :cvar VALUE_4614:
    :cvar VALUE_67:
    :cvar VALUE_7:
    :cvar VALUE_9294:
    """
    VALUE_296 = 296
    VALUE_30 = 30
    VALUE_4614 = 4614
    VALUE_67 = 67
    VALUE_7 = 7
    VALUE_9294 = 9294


@dataclass
class NistschemaSvIvAtomicUnsignedShortEnumeration2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedShort-enumeration-2"
        namespace = "NISTSchema-SV-IV-atomic-unsignedShort-enumeration-2-NS"

    value: Optional[NistschemaSvIvAtomicUnsignedShortEnumeration2Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
