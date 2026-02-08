from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedInt-enumeration-2-NS"


class NistschemaSvIvAtomicUnsignedIntEnumeration2Type(Enum):
    VALUE_1331474827 = 1331474827
    VALUE_25 = 25
    VALUE_576176 = 576176
    VALUE_944130 = 944130
    VALUE_62 = 62
    VALUE_46 = 46
    VALUE_5135198 = 5135198
    VALUE_2157977 = 2157977
    VALUE_311 = 311


@dataclass(kw_only=True)
class NistschemaSvIvAtomicUnsignedIntEnumeration2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedInt-enumeration-2"
        namespace = "NISTSchema-SV-IV-atomic-unsignedInt-enumeration-2-NS"

    value: NistschemaSvIvAtomicUnsignedIntEnumeration2Type = field()
