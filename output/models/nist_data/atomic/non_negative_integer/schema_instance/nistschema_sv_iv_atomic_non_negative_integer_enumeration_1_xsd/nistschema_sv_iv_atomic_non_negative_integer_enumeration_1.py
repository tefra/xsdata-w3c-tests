from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-nonNegativeInteger-enumeration-1-NS"


class NistschemaSvIvAtomicNonNegativeIntegerEnumeration1Type(Enum):
    VALUE_95273492 = 95273492
    VALUE_65117369587117 = 65117369587117
    VALUE_63 = 63
    VALUE_566057831 = 566057831
    VALUE_75769970879 = 75769970879
    VALUE_61084065764 = 61084065764
    VALUE_49778069509229 = 49778069509229


@dataclass
class NistschemaSvIvAtomicNonNegativeIntegerEnumeration1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-nonNegativeInteger-enumeration-1"
        namespace = (
            "NISTSchema-SV-IV-atomic-nonNegativeInteger-enumeration-1-NS"
        )

    value: Optional[NistschemaSvIvAtomicNonNegativeIntegerEnumeration1Type] = (
        field(
            default=None,
            metadata={
                "required": True,
            },
        )
    )
