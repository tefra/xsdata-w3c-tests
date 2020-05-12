from decimal import Decimal
from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-decimal-enumeration-1-NS"


class NistschemaSvIvAtomicDecimalEnumeration1Type(Enum):
    """
    :cvar VALUE_0_774:
    :cvar VALUE_885368_72:
    :cvar VALUE_8_63882452:
    :cvar VALUE_MINUS_0_92:
    :cvar VALUE_549_95:
    :cvar VALUE_MINUS_1914_0:
    """
    VALUE_0_774 = "0.774"
    VALUE_885368_72 = "885368.72"
    VALUE_8_63882452 = "8.63882452"
    VALUE_MINUS_0_92 = "-0.92"
    VALUE_549_95 = "549.95"
    VALUE_MINUS_1914_0 = "-1914.0"


@dataclass
class NistschemaSvIvAtomicDecimalEnumeration1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-decimal-enumeration-1"
        namespace = "NISTSchema-SV-IV-atomic-decimal-enumeration-1-NS"

    value: Optional[NistschemaSvIvAtomicDecimalEnumeration1Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
