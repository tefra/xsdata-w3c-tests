from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-int-enumeration-1-NS"


class NistschemaSvIvAtomicIntEnumeration1Type(Enum):
    VALUE_MINUS_8 = -8
    VALUE_MINUS_48251 = -48251
    VALUE_MINUS_726612373 = -726612373
    VALUE_7142 = 7142
    VALUE_MINUS_2212763 = -2212763
    VALUE_MINUS_532985353 = -532985353


@dataclass
class NistschemaSvIvAtomicIntEnumeration1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-int-enumeration-1"
        namespace = "NISTSchema-SV-IV-atomic-int-enumeration-1-NS"

    value: Optional[NistschemaSvIvAtomicIntEnumeration1Type] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
