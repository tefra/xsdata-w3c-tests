from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-short-enumeration-2-NS"


class NistschemaSvIvAtomicShortEnumeration2Type(Enum):
    VALUE_4 = 4
    VALUE_MINUS_7086 = -7086
    VALUE_154 = 154
    VALUE_589 = 589
    VALUE_3 = 3
    VALUE_MINUS_32768 = -32768
    VALUE_78 = 78
    VALUE_MINUS_888 = -888


@dataclass(kw_only=True)
class NistschemaSvIvAtomicShortEnumeration2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-short-enumeration-2"
        namespace = "NISTSchema-SV-IV-atomic-short-enumeration-2-NS"

    value: NistschemaSvIvAtomicShortEnumeration2Type = field()
