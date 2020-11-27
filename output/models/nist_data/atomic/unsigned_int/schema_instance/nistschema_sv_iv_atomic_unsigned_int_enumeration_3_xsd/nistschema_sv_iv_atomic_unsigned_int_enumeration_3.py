from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedInt-enumeration-3-NS"


class NistschemaSvIvAtomicUnsignedIntEnumeration3Type(Enum):
    VALUE_47 = 47
    VALUE_2421249 = 2421249
    VALUE_90949193 = 90949193
    VALUE_6248 = 6248
    VALUE_70884037 = 70884037
    VALUE_959 = 959
    VALUE_8001 = 8001
    VALUE_9175 = 9175


@dataclass
class NistschemaSvIvAtomicUnsignedIntEnumeration3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedInt-enumeration-3"
        namespace = "NISTSchema-SV-IV-atomic-unsignedInt-enumeration-3-NS"

    value: Optional[NistschemaSvIvAtomicUnsignedIntEnumeration3Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
