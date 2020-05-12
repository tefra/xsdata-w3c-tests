from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-long-enumeration-3-NS"


class NistschemaSvIvAtomicLongEnumeration3Type(Enum):
    """
    :cvar VALUE_43:
    :cvar VALUE_MINUS_2032980968765:
    :cvar VALUE_34853718286:
    :cvar VALUE_MINUS_368:
    :cvar VALUE_80579055795489529:
    :cvar VALUE_282076:
    :cvar VALUE_MINUS_4722:
    :cvar VALUE_MINUS_12200:
    :cvar VALUE_4812:
    """
    VALUE_43 = 43
    VALUE_MINUS_2032980968765 = -2032980968765
    VALUE_34853718286 = 34853718286
    VALUE_MINUS_368 = -368
    VALUE_80579055795489529 = 80579055795489529
    VALUE_282076 = 282076
    VALUE_MINUS_4722 = -4722
    VALUE_MINUS_12200 = -12200
    VALUE_4812 = 4812


@dataclass
class NistschemaSvIvAtomicLongEnumeration3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-long-enumeration-3"
        namespace = "NISTSchema-SV-IV-atomic-long-enumeration-3-NS"

    value: Optional[NistschemaSvIvAtomicLongEnumeration3Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
