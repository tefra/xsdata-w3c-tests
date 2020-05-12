from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-int-enumeration-2-NS"


class NistschemaSvIvAtomicIntEnumeration2Type(Enum):
    """
    :cvar VALUE_MINUS_2147483648:
    :cvar VALUE_516405021:
    :cvar VALUE_997702013:
    :cvar VALUE_MINUS_4389:
    :cvar VALUE_MINUS_279694555:
    :cvar VALUE_2147483647:
    :cvar VALUE_MINUS_8333939:
    :cvar VALUE_68011:
    :cvar VALUE_376934:
    """
    VALUE_MINUS_2147483648 = -2147483648
    VALUE_516405021 = 516405021
    VALUE_997702013 = 997702013
    VALUE_MINUS_4389 = -4389
    VALUE_MINUS_279694555 = -279694555
    VALUE_2147483647 = 2147483647
    VALUE_MINUS_8333939 = -8333939
    VALUE_68011 = 68011
    VALUE_376934 = 376934


@dataclass
class NistschemaSvIvAtomicIntEnumeration2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-int-enumeration-2"
        namespace = "NISTSchema-SV-IV-atomic-int-enumeration-2-NS"

    value: Optional[NistschemaSvIvAtomicIntEnumeration2Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
