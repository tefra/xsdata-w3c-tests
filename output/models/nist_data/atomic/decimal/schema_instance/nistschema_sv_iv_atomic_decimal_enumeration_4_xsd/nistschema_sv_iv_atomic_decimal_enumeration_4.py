from decimal import Decimal
from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-decimal-enumeration-4-NS"


class NistschemaSvIvAtomicDecimalEnumeration4Type(Enum):
    """
    :cvar VALUE_613_87:
    :cvar VALUE_1906433845_89:
    :cvar VALUE_MINUS_2_39446916113:
    :cvar VALUE_MINUS_5286034_1:
    :cvar VALUE_8838363181_0150:
    """
    VALUE_613_87 = "613.87"
    VALUE_1906433845_89 = "1906433845.89"
    VALUE_MINUS_2_39446916113 = "-2.39446916113"
    VALUE_MINUS_5286034_1 = "-5286034.1"
    VALUE_8838363181_0150 = "8838363181.0150"


@dataclass
class NistschemaSvIvAtomicDecimalEnumeration4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-decimal-enumeration-4"
        namespace = "NISTSchema-SV-IV-atomic-decimal-enumeration-4-NS"

    value: Optional[NistschemaSvIvAtomicDecimalEnumeration4Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
