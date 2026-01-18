from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedShort-enumeration-5-NS"


class NistschemaSvIvAtomicUnsignedShortEnumeration5Type(Enum):
    VALUE_3386 = 3386
    VALUE_700 = 700
    VALUE_1 = 1
    VALUE_2341 = 2341
    VALUE_65535 = 65535
    VALUE_88 = 88
    VALUE_3784 = 3784
    VALUE_870 = 870


@dataclass(kw_only=True)
class NistschemaSvIvAtomicUnsignedShortEnumeration5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedShort-enumeration-5"
        namespace = "NISTSchema-SV-IV-atomic-unsignedShort-enumeration-5-NS"

    value: NistschemaSvIvAtomicUnsignedShortEnumeration5Type = field(
        metadata={
            "required": True,
        }
    )
