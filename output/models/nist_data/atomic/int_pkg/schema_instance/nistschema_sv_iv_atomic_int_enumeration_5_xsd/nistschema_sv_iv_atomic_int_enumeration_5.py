from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-int-enumeration-5-NS"


class NistschemaSvIvAtomicIntEnumeration5Type(Enum):
    VALUE_MINUS_765383 = -765383
    VALUE_MINUS_878521 = -878521
    VALUE_MINUS_642 = -642
    VALUE_231 = 231
    VALUE_MINUS_2 = -2


@dataclass(kw_only=True)
class NistschemaSvIvAtomicIntEnumeration5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-int-enumeration-5"
        namespace = "NISTSchema-SV-IV-atomic-int-enumeration-5-NS"

    value: NistschemaSvIvAtomicIntEnumeration5Type = field()
