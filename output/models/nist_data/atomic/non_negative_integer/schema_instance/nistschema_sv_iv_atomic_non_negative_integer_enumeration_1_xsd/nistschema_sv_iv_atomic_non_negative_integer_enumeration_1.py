from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-nonNegativeInteger-enumeration-1-NS"


class NistschemaSvIvAtomicNonNegativeIntegerEnumeration1Type(Enum):
    VALUE_95273492 = 95273492
    VALUE_65117369587117 = 65117369587117
    VALUE_63 = 63
    VALUE_566057831 = 566057831
    VALUE_75769970879 = 75769970879
    VALUE_61084065764 = 61084065764
    VALUE_49778069509229 = 49778069509229


@dataclass(kw_only=True)
class NistschemaSvIvAtomicNonNegativeIntegerEnumeration1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-nonNegativeInteger-enumeration-1"
        namespace = (
            "NISTSchema-SV-IV-atomic-nonNegativeInteger-enumeration-1-NS"
        )

    value: NistschemaSvIvAtomicNonNegativeIntegerEnumeration1Type = field(
        metadata={
            "required": True,
        }
    )
