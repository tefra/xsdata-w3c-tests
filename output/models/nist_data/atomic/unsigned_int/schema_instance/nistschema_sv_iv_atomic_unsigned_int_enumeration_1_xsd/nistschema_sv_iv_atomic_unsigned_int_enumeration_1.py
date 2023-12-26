from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedInt-enumeration-1-NS"


class NistschemaSvIvAtomicUnsignedIntEnumeration1Type(Enum):
    VALUE_80391676 = 80391676
    VALUE_162 = 162
    VALUE_13943339 = 13943339
    VALUE_582 = 582
    VALUE_367952057 = 367952057
    VALUE_283609 = 283609
    VALUE_844 = 844


@dataclass
class NistschemaSvIvAtomicUnsignedIntEnumeration1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedInt-enumeration-1"
        namespace = "NISTSchema-SV-IV-atomic-unsignedInt-enumeration-1-NS"

    value: Optional[NistschemaSvIvAtomicUnsignedIntEnumeration1Type] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
