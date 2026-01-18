from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-integer-enumeration-2-NS"


class NistschemaSvIvAtomicIntegerEnumeration2Type(Enum):
    VALUE_MINUS_648311529 = -648311529
    VALUE_45817917 = 45817917
    VALUE_MINUS_54 = -54
    VALUE_94122922748785 = 94122922748785
    VALUE_MINUS_246897894064838530 = -246897894064838530
    VALUE_MINUS_7816621 = -7816621
    VALUE_MINUS_76931211351 = -76931211351
    VALUE_1654495802745 = 1654495802745


@dataclass(kw_only=True)
class NistschemaSvIvAtomicIntegerEnumeration2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-integer-enumeration-2"
        namespace = "NISTSchema-SV-IV-atomic-integer-enumeration-2-NS"

    value: NistschemaSvIvAtomicIntegerEnumeration2Type = field(
        metadata={
            "required": True,
        }
    )
