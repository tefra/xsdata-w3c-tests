from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-integer-enumeration-5-NS"


class NistschemaSvIvAtomicIntegerEnumeration5Type(Enum):
    VALUE_MINUS_165130515156176 = -165130515156176
    VALUE_MINUS_4149 = -4149
    VALUE_848 = 848
    VALUE_86 = 86
    VALUE_3411676615506539 = 3411676615506539
    VALUE_42603 = 42603
    VALUE_499220832 = 499220832


@dataclass(kw_only=True)
class NistschemaSvIvAtomicIntegerEnumeration5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-integer-enumeration-5"
        namespace = "NISTSchema-SV-IV-atomic-integer-enumeration-5-NS"

    value: NistschemaSvIvAtomicIntegerEnumeration5Type = field()
