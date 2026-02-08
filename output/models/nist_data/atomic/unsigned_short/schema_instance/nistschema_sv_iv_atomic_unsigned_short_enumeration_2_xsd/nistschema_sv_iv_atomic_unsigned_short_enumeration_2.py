from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedShort-enumeration-2-NS"


class NistschemaSvIvAtomicUnsignedShortEnumeration2Type(Enum):
    VALUE_9294 = 9294
    VALUE_4614 = 4614
    VALUE_296 = 296
    VALUE_7 = 7
    VALUE_30 = 30
    VALUE_67 = 67


@dataclass(kw_only=True)
class NistschemaSvIvAtomicUnsignedShortEnumeration2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedShort-enumeration-2"
        namespace = "NISTSchema-SV-IV-atomic-unsignedShort-enumeration-2-NS"

    value: NistschemaSvIvAtomicUnsignedShortEnumeration2Type = field()
