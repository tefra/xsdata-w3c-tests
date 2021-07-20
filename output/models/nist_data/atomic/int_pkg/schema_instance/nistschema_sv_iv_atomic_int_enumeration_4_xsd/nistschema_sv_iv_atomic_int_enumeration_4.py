from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-int-enumeration-4-NS"


class NistschemaSvIvAtomicIntEnumeration4Type(Enum):
    VALUE_762 = 762
    VALUE_MINUS_7786609 = -7786609
    VALUE_13025 = 13025
    VALUE_444723 = 444723
    VALUE_628279555 = 628279555
    VALUE_MINUS_929293 = -929293
    VALUE_2147483647 = 2147483647
    VALUE_994943306 = 994943306


@dataclass
class NistschemaSvIvAtomicIntEnumeration4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-int-enumeration-4"
        namespace = "NISTSchema-SV-IV-atomic-int-enumeration-4-NS"

    value: Optional[NistschemaSvIvAtomicIntEnumeration4Type] = field(
        default=None
    )
