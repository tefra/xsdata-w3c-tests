from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-positiveInteger-enumeration-2-NS"


class NistschemaSvIvAtomicPositiveIntegerEnumeration2Type(Enum):
    """
    :cvar VALUE_853441:
    :cvar VALUE_5705619952894463:
    :cvar VALUE_468315652460615:
    :cvar VALUE_54802934845216066:
    :cvar VALUE_10:
    :cvar VALUE_801:
    :cvar VALUE_8410074843393:
    :cvar VALUE_87378193514885904:
    :cvar VALUE_127831830298:
    """
    VALUE_853441 = 853441
    VALUE_5705619952894463 = 5705619952894463
    VALUE_468315652460615 = 468315652460615
    VALUE_54802934845216066 = 54802934845216066
    VALUE_10 = 10
    VALUE_801 = 801
    VALUE_8410074843393 = 8410074843393
    VALUE_87378193514885904 = 87378193514885904
    VALUE_127831830298 = 127831830298


@dataclass
class NistschemaSvIvAtomicPositiveIntegerEnumeration2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-positiveInteger-enumeration-2"
        namespace = "NISTSchema-SV-IV-atomic-positiveInteger-enumeration-2-NS"

    value: Optional[NistschemaSvIvAtomicPositiveIntegerEnumeration2Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
