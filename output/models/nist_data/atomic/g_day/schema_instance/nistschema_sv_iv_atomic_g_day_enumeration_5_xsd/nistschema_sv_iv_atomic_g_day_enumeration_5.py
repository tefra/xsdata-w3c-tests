from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gDay-enumeration-5-NS"


class NistschemaSvIvAtomicGDayEnumeration5Type(Enum):
    VALUE_21 = "---21"
    VALUE_23 = "---23"
    VALUE_13 = "---13"
    VALUE_26 = "---26"
    VALUE_24 = "---24"
    VALUE_18 = "---18"
    VALUE_30 = "---30"
    VALUE_14 = "---14"


@dataclass
class NistschemaSvIvAtomicGDayEnumeration5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gDay-enumeration-5"
        namespace = "NISTSchema-SV-IV-atomic-gDay-enumeration-5-NS"

    value: Optional[NistschemaSvIvAtomicGDayEnumeration5Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
