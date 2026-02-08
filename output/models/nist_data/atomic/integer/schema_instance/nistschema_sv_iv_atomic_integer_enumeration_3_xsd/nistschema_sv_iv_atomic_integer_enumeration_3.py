from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-integer-enumeration-3-NS"


class NistschemaSvIvAtomicIntegerEnumeration3Type(Enum):
    VALUE_3 = 3
    VALUE_522 = 522
    VALUE_MINUS_34 = -34
    VALUE_MINUS_685416 = -685416
    VALUE_MINUS_567825257 = -567825257
    VALUE_MINUS_451904674315973253 = -451904674315973253


@dataclass(kw_only=True)
class NistschemaSvIvAtomicIntegerEnumeration3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-integer-enumeration-3"
        namespace = "NISTSchema-SV-IV-atomic-integer-enumeration-3-NS"

    value: NistschemaSvIvAtomicIntegerEnumeration3Type = field()
