from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gDay-enumeration-1-NS"


class NistschemaSvIvAtomicGDayEnumeration1Type(Enum):
    VALUE_15 = "---15"
    VALUE_29 = "---29"
    VALUE_30 = "---30"
    VALUE_26 = "---26"
    VALUE_16 = "---16"
    VALUE_08 = "---08"
    VALUE_18 = "---18"
    VALUE_07 = "---07"


@dataclass
class NistschemaSvIvAtomicGDayEnumeration1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gDay-enumeration-1"
        namespace = "NISTSchema-SV-IV-atomic-gDay-enumeration-1-NS"

    value: Optional[NistschemaSvIvAtomicGDayEnumeration1Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
