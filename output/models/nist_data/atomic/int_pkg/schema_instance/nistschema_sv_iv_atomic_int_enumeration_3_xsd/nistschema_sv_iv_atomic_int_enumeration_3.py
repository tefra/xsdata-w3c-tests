from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-int-enumeration-3-NS"


class NistschemaSvIvAtomicIntEnumeration3Type(Enum):
    VALUE_2147483647 = 2147483647
    VALUE_70977758 = 70977758
    VALUE_323669986 = 323669986
    VALUE_MINUS_314 = -314
    VALUE_MINUS_53685045 = -53685045
    VALUE_9391921 = 9391921
    VALUE_43292492 = 43292492
    VALUE_MINUS_2142090 = -2142090


@dataclass
class NistschemaSvIvAtomicIntEnumeration3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-int-enumeration-3"
        namespace = "NISTSchema-SV-IV-atomic-int-enumeration-3-NS"

    value: Optional[NistschemaSvIvAtomicIntEnumeration3Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
