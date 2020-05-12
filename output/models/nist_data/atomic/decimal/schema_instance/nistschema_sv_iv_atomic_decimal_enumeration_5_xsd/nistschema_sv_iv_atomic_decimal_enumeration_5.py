from decimal import Decimal
from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-decimal-enumeration-5-NS"


class NistschemaSvIvAtomicDecimalEnumeration5Type(Enum):
    """
    :cvar VALUE_0_3316:
    :cvar VALUE_337920_941:
    :cvar VALUE_6_9307231814179:
    :cvar VALUE_856_89:
    :cvar VALUE_MINUS_0_61:
    :cvar VALUE_MINUS_150:
    :cvar VALUE_MINUS_82_78605057:
    """
    VALUE_0_3316 = "0.3316"
    VALUE_337920_941 = "337920.941"
    VALUE_6_9307231814179 = "6.9307231814179"
    VALUE_856_89 = "856.89"
    VALUE_MINUS_0_61 = "-0.61"
    VALUE_MINUS_150 = "-150"
    VALUE_MINUS_82_78605057 = "-82.78605057"


@dataclass
class NistschemaSvIvAtomicDecimalEnumeration5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-decimal-enumeration-5"
        namespace = "NISTSchema-SV-IV-atomic-decimal-enumeration-5-NS"

    value: Optional[NistschemaSvIvAtomicDecimalEnumeration5Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
