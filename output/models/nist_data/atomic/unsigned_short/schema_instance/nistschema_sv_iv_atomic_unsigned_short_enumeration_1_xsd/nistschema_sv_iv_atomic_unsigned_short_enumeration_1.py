from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedShort-enumeration-1-NS"


class NistschemaSvIvAtomicUnsignedShortEnumeration1Type(Enum):
    VALUE_603 = 603
    VALUE_121 = 121
    VALUE_51760 = 51760
    VALUE_65535 = 65535
    VALUE_357 = 357
    VALUE_272 = 272
    VALUE_570 = 570
    VALUE_28 = 28


@dataclass
class NistschemaSvIvAtomicUnsignedShortEnumeration1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedShort-enumeration-1"
        namespace = "NISTSchema-SV-IV-atomic-unsignedShort-enumeration-1-NS"

    value: Optional[NistschemaSvIvAtomicUnsignedShortEnumeration1Type] = field(
        default=None
    )
