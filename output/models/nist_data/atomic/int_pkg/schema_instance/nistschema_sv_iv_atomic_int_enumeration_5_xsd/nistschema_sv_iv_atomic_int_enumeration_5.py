from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-int-enumeration-5-NS"


class NistschemaSvIvAtomicIntEnumeration5Type(Enum):
    """
    :cvar VALUE_MINUS_765383:
    :cvar VALUE_MINUS_878521:
    :cvar VALUE_MINUS_642:
    :cvar VALUE_231:
    :cvar VALUE_MINUS_2:
    """
    VALUE_MINUS_765383 = -765383
    VALUE_MINUS_878521 = -878521
    VALUE_MINUS_642 = -642
    VALUE_231 = 231
    VALUE_MINUS_2 = -2


@dataclass
class NistschemaSvIvAtomicIntEnumeration5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-int-enumeration-5"
        namespace = "NISTSchema-SV-IV-atomic-int-enumeration-5-NS"

    value: Optional[NistschemaSvIvAtomicIntEnumeration5Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
