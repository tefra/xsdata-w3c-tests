from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYearMonth-enumeration-4-NS"


class NistschemaSvIvAtomicGYearMonthEnumeration4Type(Enum):
    VALUE_1984_02 = "1984-02"
    VALUE_2007_01 = "2007-01"
    VALUE_2027_09 = "2027-09"
    VALUE_1974_01 = "1974-01"
    VALUE_2006_11 = "2006-11"
    VALUE_2007_11 = "2007-11"


@dataclass
class NistschemaSvIvAtomicGYearMonthEnumeration4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYearMonth-enumeration-4"
        namespace = "NISTSchema-SV-IV-atomic-gYearMonth-enumeration-4-NS"

    value: Optional[NistschemaSvIvAtomicGYearMonthEnumeration4Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
