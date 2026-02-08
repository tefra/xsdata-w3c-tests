from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-short-enumeration-3-NS"


class NistschemaSvIvAtomicShortEnumeration3Type(Enum):
    VALUE_448 = 448
    VALUE_MINUS_172 = -172
    VALUE_MINUS_9314 = -9314
    VALUE_740 = 740
    VALUE_MINUS_570 = -570


@dataclass(kw_only=True)
class NistschemaSvIvAtomicShortEnumeration3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-short-enumeration-3"
        namespace = "NISTSchema-SV-IV-atomic-short-enumeration-3-NS"

    value: NistschemaSvIvAtomicShortEnumeration3Type = field()
