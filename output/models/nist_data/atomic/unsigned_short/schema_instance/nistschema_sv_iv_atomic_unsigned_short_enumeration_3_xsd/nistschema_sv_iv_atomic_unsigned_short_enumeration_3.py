from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedShort-enumeration-3-NS"


class NistschemaSvIvAtomicUnsignedShortEnumeration3Type(Enum):
    VALUE_58929 = 58929
    VALUE_12 = 12
    VALUE_4 = 4
    VALUE_2521 = 2521
    VALUE_3449 = 3449
    VALUE_1963 = 1963
    VALUE_6997 = 6997
    VALUE_609 = 609


@dataclass
class NistschemaSvIvAtomicUnsignedShortEnumeration3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedShort-enumeration-3"
        namespace = "NISTSchema-SV-IV-atomic-unsignedShort-enumeration-3-NS"

    value: Optional[NistschemaSvIvAtomicUnsignedShortEnumeration3Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
