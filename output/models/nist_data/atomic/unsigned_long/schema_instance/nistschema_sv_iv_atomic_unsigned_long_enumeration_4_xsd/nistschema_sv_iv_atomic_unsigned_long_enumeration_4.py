from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedLong-enumeration-4-NS"


class NistschemaSvIvAtomicUnsignedLongEnumeration4Type(Enum):
    VALUE_10 = 10
    VALUE_1737393204819 = 1737393204819
    VALUE_8333904222 = 8333904222
    VALUE_5093784 = 5093784
    VALUE_50511429 = 50511429
    VALUE_602699130 = 602699130


@dataclass(kw_only=True)
class NistschemaSvIvAtomicUnsignedLongEnumeration4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedLong-enumeration-4"
        namespace = "NISTSchema-SV-IV-atomic-unsignedLong-enumeration-4-NS"

    value: NistschemaSvIvAtomicUnsignedLongEnumeration4Type = field(
        metadata={
            "required": True,
        }
    )
