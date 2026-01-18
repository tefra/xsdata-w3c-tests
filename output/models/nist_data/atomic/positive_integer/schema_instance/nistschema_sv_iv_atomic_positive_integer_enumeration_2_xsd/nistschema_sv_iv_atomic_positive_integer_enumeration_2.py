from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-positiveInteger-enumeration-2-NS"


class NistschemaSvIvAtomicPositiveIntegerEnumeration2Type(Enum):
    VALUE_853441 = 853441
    VALUE_5705619952894463 = 5705619952894463
    VALUE_468315652460615 = 468315652460615
    VALUE_54802934845216066 = 54802934845216066
    VALUE_10 = 10
    VALUE_801 = 801
    VALUE_8410074843393 = 8410074843393
    VALUE_87378193514885904 = 87378193514885904
    VALUE_127831830298 = 127831830298


@dataclass(kw_only=True)
class NistschemaSvIvAtomicPositiveIntegerEnumeration2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-positiveInteger-enumeration-2"
        namespace = "NISTSchema-SV-IV-atomic-positiveInteger-enumeration-2-NS"

    value: NistschemaSvIvAtomicPositiveIntegerEnumeration2Type = field(
        metadata={
            "required": True,
        }
    )
