from decimal import Decimal
from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-decimal-enumeration-3-NS"


class NistschemaSvIvAtomicDecimalEnumeration3Type(Enum):
    """
    :cvar VALUE_0_672:
    :cvar VALUE_0_86054905:
    :cvar VALUE_840:
    :cvar VALUE_MINUS_5439_8474996:
    :cvar VALUE_MINUS_584_55228:
    :cvar VALUE_MINUS_75_62365:
    :cvar VALUE_MINUS_7_335:
    :cvar VALUE_MINUS_97585886185:
    """
    VALUE_0_672 = "0.672"
    VALUE_0_86054905 = "0.86054905"
    VALUE_840 = "840"
    VALUE_MINUS_5439_8474996 = "-5439.8474996"
    VALUE_MINUS_584_55228 = "-584.55228"
    VALUE_MINUS_75_62365 = "-75.62365"
    VALUE_MINUS_7_335 = "-7.335"
    VALUE_MINUS_97585886185 = "-97585886185"


@dataclass
class NistschemaSvIvAtomicDecimalEnumeration3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-decimal-enumeration-3"
        namespace = "NISTSchema-SV-IV-atomic-decimal-enumeration-3-NS"

    value: Optional[NistschemaSvIvAtomicDecimalEnumeration3Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
