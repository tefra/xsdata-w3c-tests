from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-int-enumeration-5-NS"


class NistschemaSvIvAtomicIntEnumeration5Type(Enum):
    VALUE_MINUS_765383 = -765383
    VALUE_MINUS_878521 = -878521
    VALUE_MINUS_642 = -642
    VALUE_231 = 231
    VALUE_MINUS_2 = -2


@dataclass
class NistschemaSvIvAtomicIntEnumeration5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-int-enumeration-5"
        namespace = "NISTSchema-SV-IV-atomic-int-enumeration-5-NS"

    value: Optional[NistschemaSvIvAtomicIntEnumeration5Type] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
