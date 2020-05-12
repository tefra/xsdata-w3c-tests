from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-short-enumeration-3-NS"


class NistschemaSvIvAtomicShortEnumeration3Type(Enum):
    """
    :cvar VALUE_448:
    :cvar VALUE_MINUS_172:
    :cvar VALUE_MINUS_9314:
    :cvar VALUE_740:
    :cvar VALUE_MINUS_570:
    """
    VALUE_448 = 448
    VALUE_MINUS_172 = -172
    VALUE_MINUS_9314 = -9314
    VALUE_740 = 740
    VALUE_MINUS_570 = -570


@dataclass
class NistschemaSvIvAtomicShortEnumeration3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-short-enumeration-3"
        namespace = "NISTSchema-SV-IV-atomic-short-enumeration-3-NS"

    value: Optional[NistschemaSvIvAtomicShortEnumeration3Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
