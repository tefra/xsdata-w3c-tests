from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-int-enumeration-4-NS"


class NistschemaSvIvAtomicIntEnumeration4Type(Enum):
    """
    :cvar VALUE_MINUS_7786609:
    :cvar VALUE_MINUS_929293:
    :cvar VALUE_13025:
    :cvar VALUE_2147483647:
    :cvar VALUE_444723:
    :cvar VALUE_628279555:
    :cvar VALUE_762:
    :cvar VALUE_994943306:
    """
    VALUE_MINUS_7786609 = -7786609
    VALUE_MINUS_929293 = -929293
    VALUE_13025 = 13025
    VALUE_2147483647 = 2147483647
    VALUE_444723 = 444723
    VALUE_628279555 = 628279555
    VALUE_762 = 762
    VALUE_994943306 = 994943306


@dataclass
class NistschemaSvIvAtomicIntEnumeration4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-int-enumeration-4"
        namespace = "NISTSchema-SV-IV-atomic-int-enumeration-4-NS"

    value: Optional[NistschemaSvIvAtomicIntEnumeration4Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
