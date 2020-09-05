from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-long-enumeration-1-NS"


class NistschemaSvIvAtomicLongEnumeration1Type(Enum):
    """
    :cvar VALUE_67417897408:
    :cvar VALUE_445463702:
    :cvar VALUE_11686316:
    :cvar VALUE_MINUS_223498733:
    :cvar VALUE_MINUS_5496081750511:
    :cvar VALUE_MINUS_4233583602889:
    """
    VALUE_67417897408 = 67417897408
    VALUE_445463702 = 445463702
    VALUE_11686316 = 11686316
    VALUE_MINUS_223498733 = -223498733
    VALUE_MINUS_5496081750511 = -5496081750511
    VALUE_MINUS_4233583602889 = -4233583602889


@dataclass
class NistschemaSvIvAtomicLongEnumeration1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-long-enumeration-1"
        namespace = "NISTSchema-SV-IV-atomic-long-enumeration-1-NS"

    value: Optional[NistschemaSvIvAtomicLongEnumeration1Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
