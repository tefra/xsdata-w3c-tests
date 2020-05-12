from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-integer-enumeration-3-NS"


class NistschemaSvIvAtomicIntegerEnumeration3Type(Enum):
    """
    :cvar VALUE_3:
    :cvar VALUE_522:
    :cvar VALUE_MINUS_34:
    :cvar VALUE_MINUS_451904674315973253:
    :cvar VALUE_MINUS_567825257:
    :cvar VALUE_MINUS_685416:
    """
    VALUE_3 = 3
    VALUE_522 = 522
    VALUE_MINUS_34 = -34
    VALUE_MINUS_451904674315973253 = -451904674315973253
    VALUE_MINUS_567825257 = -567825257
    VALUE_MINUS_685416 = -685416


@dataclass
class NistschemaSvIvAtomicIntegerEnumeration3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-integer-enumeration-3"
        namespace = "NISTSchema-SV-IV-atomic-integer-enumeration-3-NS"

    value: Optional[NistschemaSvIvAtomicIntegerEnumeration3Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
