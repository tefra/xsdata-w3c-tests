from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gDay-enumeration-3-NS"


class NistschemaSvIvAtomicGDayEnumeration3Type(Enum):
    VALUE_15 = "---15"
    VALUE_27 = "---27"
    VALUE_16 = "---16"
    VALUE_22 = "---22"
    VALUE_12 = "---12"
    VALUE_30 = "---30"
    VALUE_24 = "---24"
    VALUE_14 = "---14"
    VALUE_09 = "---09"


@dataclass
class NistschemaSvIvAtomicGDayEnumeration3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gDay-enumeration-3"
        namespace = "NISTSchema-SV-IV-atomic-gDay-enumeration-3-NS"

    value: Optional[NistschemaSvIvAtomicGDayEnumeration3Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
