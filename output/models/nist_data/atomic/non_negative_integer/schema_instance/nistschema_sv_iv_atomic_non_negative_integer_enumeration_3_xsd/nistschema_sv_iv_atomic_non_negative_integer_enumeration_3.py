from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-nonNegativeInteger-enumeration-3-NS"


class NistschemaSvIvAtomicNonNegativeIntegerEnumeration3Type(Enum):
    VALUE_23892815 = 23892815
    VALUE_90576835920 = 90576835920
    VALUE_424484 = 424484
    VALUE_79896 = 79896
    VALUE_9556157928 = 9556157928
    VALUE_9176 = 9176
    VALUE_802100066184431 = 802100066184431
    VALUE_668936 = 668936
    VALUE_849475711356152407 = 849475711356152407
    VALUE_71162303480519 = 71162303480519


@dataclass(kw_only=True)
class NistschemaSvIvAtomicNonNegativeIntegerEnumeration3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-nonNegativeInteger-enumeration-3"
        namespace = (
            "NISTSchema-SV-IV-atomic-nonNegativeInteger-enumeration-3-NS"
        )

    value: NistschemaSvIvAtomicNonNegativeIntegerEnumeration3Type = field(
        metadata={
            "required": True,
        }
    )
