from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedLong-enumeration-4-NS"


class NistschemaSvIvAtomicUnsignedLongEnumeration4Type(Enum):
    """
    :cvar VALUE_10:
    :cvar VALUE_1737393204819:
    :cvar VALUE_50511429:
    :cvar VALUE_5093784:
    :cvar VALUE_602699130:
    :cvar VALUE_8333904222:
    """
    VALUE_10 = 10
    VALUE_1737393204819 = 1737393204819
    VALUE_50511429 = 50511429
    VALUE_5093784 = 5093784
    VALUE_602699130 = 602699130
    VALUE_8333904222 = 8333904222


@dataclass
class NistschemaSvIvAtomicUnsignedLongEnumeration4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedLong-enumeration-4"
        namespace = "NISTSchema-SV-IV-atomic-unsignedLong-enumeration-4-NS"

    value: Optional[NistschemaSvIvAtomicUnsignedLongEnumeration4Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )