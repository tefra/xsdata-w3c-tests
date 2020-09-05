from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-nonPositiveInteger-enumeration-1-NS"


class NistschemaSvIvAtomicNonPositiveIntegerEnumeration1Type(Enum):
    """
    :cvar VALUE_MINUS_2:
    :cvar VALUE_MINUS_9433249751626:
    :cvar VALUE_MINUS_490343697:
    :cvar VALUE_MINUS_34057323631:
    :cvar VALUE_MINUS_4061916853:
    :cvar VALUE_MINUS_761218:
    """
    VALUE_MINUS_2 = -2
    VALUE_MINUS_9433249751626 = -9433249751626
    VALUE_MINUS_490343697 = -490343697
    VALUE_MINUS_34057323631 = -34057323631
    VALUE_MINUS_4061916853 = -4061916853
    VALUE_MINUS_761218 = -761218


@dataclass
class NistschemaSvIvAtomicNonPositiveIntegerEnumeration1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-nonPositiveInteger-enumeration-1"
        namespace = "NISTSchema-SV-IV-atomic-nonPositiveInteger-enumeration-1-NS"

    value: Optional[NistschemaSvIvAtomicNonPositiveIntegerEnumeration1Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
