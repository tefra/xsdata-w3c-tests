from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedLong-enumeration-4-NS"


class NistschemaSvIvAtomicUnsignedLongEnumeration4Type(Enum):
    VALUE_10 = 10
    VALUE_1737393204819 = 1737393204819
    VALUE_8333904222 = 8333904222
    VALUE_5093784 = 5093784
    VALUE_50511429 = 50511429
    VALUE_602699130 = 602699130


@dataclass
class NistschemaSvIvAtomicUnsignedLongEnumeration4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedLong-enumeration-4"
        namespace = "NISTSchema-SV-IV-atomic-unsignedLong-enumeration-4-NS"

    value: Optional[NistschemaSvIvAtomicUnsignedLongEnumeration4Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
