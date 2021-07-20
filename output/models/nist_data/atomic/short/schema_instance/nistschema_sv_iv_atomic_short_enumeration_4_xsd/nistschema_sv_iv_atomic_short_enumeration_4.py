from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-short-enumeration-4-NS"


class NistschemaSvIvAtomicShortEnumeration4Type(Enum):
    VALUE_902 = 902
    VALUE_19 = 19
    VALUE_4452 = 4452
    VALUE_41 = 41
    VALUE_6 = 6
    VALUE_MINUS_8727 = -8727


@dataclass
class NistschemaSvIvAtomicShortEnumeration4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-short-enumeration-4"
        namespace = "NISTSchema-SV-IV-atomic-short-enumeration-4-NS"

    value: Optional[NistschemaSvIvAtomicShortEnumeration4Type] = field(
        default=None
    )
