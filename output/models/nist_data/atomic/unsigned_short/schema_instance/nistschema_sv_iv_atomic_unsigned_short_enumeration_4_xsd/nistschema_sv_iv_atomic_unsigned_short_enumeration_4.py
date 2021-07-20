from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedShort-enumeration-4-NS"


class NistschemaSvIvAtomicUnsignedShortEnumeration4Type(Enum):
    VALUE_3331 = 3331
    VALUE_794 = 794
    VALUE_91 = 91
    VALUE_5792 = 5792
    VALUE_5361 = 5361
    VALUE_72 = 72
    VALUE_1768 = 1768
    VALUE_37 = 37
    VALUE_464 = 464


@dataclass
class NistschemaSvIvAtomicUnsignedShortEnumeration4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedShort-enumeration-4"
        namespace = "NISTSchema-SV-IV-atomic-unsignedShort-enumeration-4-NS"

    value: Optional[NistschemaSvIvAtomicUnsignedShortEnumeration4Type] = field(
        default=None
    )
