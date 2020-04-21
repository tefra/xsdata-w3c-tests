from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-nonNegativeInteger-enumeration-3-NS"


class NistschemaSvIvAtomicNonNegativeIntegerEnumeration3Type(Enum):
    """
    :cvar VALUE_23892815:
    :cvar VALUE_424484:
    :cvar VALUE_668936:
    :cvar VALUE_71162303480519:
    :cvar VALUE_79896:
    :cvar VALUE_802100066184431:
    :cvar VALUE_849475711356152407:
    :cvar VALUE_90576835920:
    :cvar VALUE_9176:
    :cvar VALUE_9556157928:
    """
    VALUE_23892815 = 23892815
    VALUE_424484 = 424484
    VALUE_668936 = 668936
    VALUE_71162303480519 = 71162303480519
    VALUE_79896 = 79896
    VALUE_802100066184431 = 802100066184431
    VALUE_849475711356152407 = 849475711356152407
    VALUE_90576835920 = 90576835920
    VALUE_9176 = 9176
    VALUE_9556157928 = 9556157928


@dataclass
class NistschemaSvIvAtomicNonNegativeIntegerEnumeration3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-nonNegativeInteger-enumeration-3"
        namespace = "NISTSchema-SV-IV-atomic-nonNegativeInteger-enumeration-3-NS"

    value: Optional[NistschemaSvIvAtomicNonNegativeIntegerEnumeration3Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
