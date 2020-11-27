from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gDay-enumeration-2-NS"


class NistschemaSvIvAtomicGDayEnumeration2Type(Enum):
    VALUE_04 = "---04"
    VALUE_22 = "---22"
    VALUE_20 = "---20"
    VALUE_18 = "---18"
    VALUE_12 = "---12"
    VALUE_10 = "---10"
    VALUE_08 = "---08"


@dataclass
class NistschemaSvIvAtomicGDayEnumeration2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gDay-enumeration-2"
        namespace = "NISTSchema-SV-IV-atomic-gDay-enumeration-2-NS"

    value: Optional[NistschemaSvIvAtomicGDayEnumeration2Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
