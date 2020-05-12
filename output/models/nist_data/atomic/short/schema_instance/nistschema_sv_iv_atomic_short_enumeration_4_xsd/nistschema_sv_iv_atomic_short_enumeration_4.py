from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-short-enumeration-4-NS"


class NistschemaSvIvAtomicShortEnumeration4Type(Enum):
    """
    :cvar VALUE_902:
    :cvar VALUE_19:
    :cvar VALUE_4452:
    :cvar VALUE_41:
    :cvar VALUE_6:
    :cvar VALUE_MINUS_8727:
    """
    VALUE_902 = 902
    VALUE_19 = 19
    VALUE_4452 = 4452
    VALUE_41 = 41
    VALUE_6 = 6
    VALUE_MINUS_8727 = -8727


@dataclass
class NistschemaSvIvAtomicShortEnumeration4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-short-enumeration-4"
        namespace = "NISTSchema-SV-IV-atomic-short-enumeration-4-NS"

    value: Optional[NistschemaSvIvAtomicShortEnumeration4Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
