from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-integer-enumeration-1-NS"


class NistschemaSvIvAtomicIntegerEnumeration1Type(Enum):
    VALUE_MINUS_79656589620485973 = -79656589620485973
    VALUE_61 = 61
    VALUE_5609571936 = 5609571936
    VALUE_MINUS_4739709191124 = -4739709191124
    VALUE_629890508912219 = 629890508912219
    VALUE_MINUS_820 = -820
    VALUE_MINUS_635117251034 = -635117251034
    VALUE_371694697980 = 371694697980


@dataclass(kw_only=True)
class NistschemaSvIvAtomicIntegerEnumeration1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-integer-enumeration-1"
        namespace = "NISTSchema-SV-IV-atomic-integer-enumeration-1-NS"

    value: NistschemaSvIvAtomicIntegerEnumeration1Type = field(
        metadata={
            "required": True,
        }
    )
