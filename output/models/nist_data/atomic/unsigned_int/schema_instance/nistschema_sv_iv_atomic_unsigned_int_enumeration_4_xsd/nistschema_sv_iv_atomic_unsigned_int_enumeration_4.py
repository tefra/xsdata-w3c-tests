from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedInt-enumeration-4-NS"


class NistschemaSvIvAtomicUnsignedIntEnumeration4Type(Enum):
    VALUE_47 = 47
    VALUE_9906 = 9906
    VALUE_271268 = 271268
    VALUE_18558 = 18558
    VALUE_969778623 = 969778623
    VALUE_237992966 = 237992966


@dataclass(kw_only=True)
class NistschemaSvIvAtomicUnsignedIntEnumeration4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedInt-enumeration-4"
        namespace = "NISTSchema-SV-IV-atomic-unsignedInt-enumeration-4-NS"

    value: NistschemaSvIvAtomicUnsignedIntEnumeration4Type = field()
