from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedShort-enumeration-1-NS"


class NistschemaSvIvAtomicUnsignedShortEnumeration1Type(Enum):
    VALUE_603 = 603
    VALUE_121 = 121
    VALUE_51760 = 51760
    VALUE_65535 = 65535
    VALUE_357 = 357
    VALUE_272 = 272
    VALUE_570 = 570
    VALUE_28 = 28


@dataclass(kw_only=True)
class NistschemaSvIvAtomicUnsignedShortEnumeration1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedShort-enumeration-1"
        namespace = "NISTSchema-SV-IV-atomic-unsignedShort-enumeration-1-NS"

    value: NistschemaSvIvAtomicUnsignedShortEnumeration1Type = field()
