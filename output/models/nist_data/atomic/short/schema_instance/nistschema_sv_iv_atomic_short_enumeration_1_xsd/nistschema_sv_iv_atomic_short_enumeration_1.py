from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-short-enumeration-1-NS"


class NistschemaSvIvAtomicShortEnumeration1Type(Enum):
    """
    :cvar VALUE_MINUS_8076:
    :cvar VALUE_5805:
    :cvar VALUE_11013:
    :cvar VALUE_MINUS_5:
    :cvar VALUE_7589:
    :cvar VALUE_MINUS_84:
    """
    VALUE_MINUS_8076 = -8076
    VALUE_5805 = 5805
    VALUE_11013 = 11013
    VALUE_MINUS_5 = -5
    VALUE_7589 = 7589
    VALUE_MINUS_84 = -84


@dataclass
class NistschemaSvIvAtomicShortEnumeration1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-short-enumeration-1"
        namespace = "NISTSchema-SV-IV-atomic-short-enumeration-1-NS"

    value: Optional[NistschemaSvIvAtomicShortEnumeration1Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
