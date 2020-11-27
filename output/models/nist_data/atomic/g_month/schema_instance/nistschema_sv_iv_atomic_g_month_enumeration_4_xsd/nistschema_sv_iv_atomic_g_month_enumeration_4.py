from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gMonth-enumeration-4-NS"


class NistschemaSvIvAtomicGMonthEnumeration4Type(Enum):
    VALUE_07 = "--07"
    VALUE_03 = "--03"
    VALUE_05 = "--05"
    VALUE_02 = "--02"
    VALUE_10 = "--10"
    VALUE_04 = "--04"


@dataclass
class NistschemaSvIvAtomicGMonthEnumeration4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gMonth-enumeration-4"
        namespace = "NISTSchema-SV-IV-atomic-gMonth-enumeration-4-NS"

    value: Optional[NistschemaSvIvAtomicGMonthEnumeration4Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
