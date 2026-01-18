from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-positiveInteger-enumeration-1-NS"


class NistschemaSvIvAtomicPositiveIntegerEnumeration1Type(Enum):
    VALUE_29 = 29
    VALUE_3059918349066803 = 3059918349066803
    VALUE_44881 = 44881
    VALUE_557 = 557
    VALUE_39237065970202644 = 39237065970202644
    VALUE_101001635697 = 101001635697
    VALUE_7652 = 7652
    VALUE_408576971836088 = 408576971836088


@dataclass(kw_only=True)
class NistschemaSvIvAtomicPositiveIntegerEnumeration1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-positiveInteger-enumeration-1"
        namespace = "NISTSchema-SV-IV-atomic-positiveInteger-enumeration-1-NS"

    value: NistschemaSvIvAtomicPositiveIntegerEnumeration1Type = field(
        metadata={
            "required": True,
        }
    )
