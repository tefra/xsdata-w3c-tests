from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-integer-enumeration-5-NS"


class NistschemaSvIvAtomicIntegerEnumeration5Type(Enum):
    VALUE_MINUS_165130515156176 = -165130515156176
    VALUE_MINUS_4149 = -4149
    VALUE_848 = 848
    VALUE_86 = 86
    VALUE_3411676615506539 = 3411676615506539
    VALUE_42603 = 42603
    VALUE_499220832 = 499220832


@dataclass
class NistschemaSvIvAtomicIntegerEnumeration5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-integer-enumeration-5"
        namespace = "NISTSchema-SV-IV-atomic-integer-enumeration-5-NS"

    value: Optional[NistschemaSvIvAtomicIntegerEnumeration5Type] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
