from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-integer-enumeration-2-NS"


class NistschemaSvIvAtomicIntegerEnumeration2Type(Enum):
    """
    :cvar VALUE_MINUS_246897894064838530:
    :cvar VALUE_MINUS_54:
    :cvar VALUE_MINUS_648311529:
    :cvar VALUE_MINUS_76931211351:
    :cvar VALUE_MINUS_7816621:
    :cvar VALUE_1654495802745:
    :cvar VALUE_45817917:
    :cvar VALUE_94122922748785:
    """
    VALUE_MINUS_246897894064838530 = -246897894064838530
    VALUE_MINUS_54 = -54
    VALUE_MINUS_648311529 = -648311529
    VALUE_MINUS_76931211351 = -76931211351
    VALUE_MINUS_7816621 = -7816621
    VALUE_1654495802745 = 1654495802745
    VALUE_45817917 = 45817917
    VALUE_94122922748785 = 94122922748785


@dataclass
class NistschemaSvIvAtomicIntegerEnumeration2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-integer-enumeration-2"
        namespace = "NISTSchema-SV-IV-atomic-integer-enumeration-2-NS"

    value: Optional[NistschemaSvIvAtomicIntegerEnumeration2Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )