from __future__ import annotations

from dataclasses import dataclass, field
from enum import IntEnum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-integer-enumeration-4-NS"


class NistschemaSvIvAtomicIntegerEnumeration4Type(IntEnum):
    VALUE_MINUS_1480745378756 = -1480745378756
    VALUE_MINUS_479 = -479
    VALUE_9967661580861324 = 9967661580861324
    VALUE_MINUS_21 = -21
    VALUE_44 = 44
    VALUE_35682594228541431 = 35682594228541431
    VALUE_759297981117 = 759297981117


@dataclass(kw_only=True)
class NistschemaSvIvAtomicIntegerEnumeration4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-integer-enumeration-4"
        namespace = "NISTSchema-SV-IV-atomic-integer-enumeration-4-NS"

    value: NistschemaSvIvAtomicIntegerEnumeration4Type = field()
