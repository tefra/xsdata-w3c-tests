from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-short-enumeration-5-NS"


class NistschemaSvIvAtomicShortEnumeration5Type(Enum):
    """
    :cvar VALUE_MINUS_45:
    :cvar VALUE_MINUS_49:
    :cvar VALUE_3112:
    :cvar VALUE_3174:
    :cvar VALUE_32767:
    :cvar VALUE_370:
    :cvar VALUE_74:
    """
    VALUE_MINUS_45 = -45
    VALUE_MINUS_49 = -49
    VALUE_3112 = 3112
    VALUE_3174 = 3174
    VALUE_32767 = 32767
    VALUE_370 = 370
    VALUE_74 = 74


@dataclass
class NistschemaSvIvAtomicShortEnumeration5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-short-enumeration-5"
        namespace = "NISTSchema-SV-IV-atomic-short-enumeration-5-NS"

    value: Optional[NistschemaSvIvAtomicShortEnumeration5Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )