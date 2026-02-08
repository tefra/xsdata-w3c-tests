from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-negativeInteger-enumeration-4-NS"


class NistschemaSvIvAtomicNegativeIntegerEnumeration4Type(Enum):
    VALUE_MINUS_87037330956252501 = -87037330956252501
    VALUE_MINUS_36619944811 = -36619944811
    VALUE_MINUS_57023 = -57023
    VALUE_MINUS_918536646 = -918536646
    VALUE_MINUS_399072682 = -399072682
    VALUE_MINUS_39747055905837447 = -39747055905837447
    VALUE_MINUS_941633341616753 = -941633341616753


@dataclass(kw_only=True)
class NistschemaSvIvAtomicNegativeIntegerEnumeration4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-negativeInteger-enumeration-4"
        namespace = "NISTSchema-SV-IV-atomic-negativeInteger-enumeration-4-NS"

    value: NistschemaSvIvAtomicNegativeIntegerEnumeration4Type = field()
