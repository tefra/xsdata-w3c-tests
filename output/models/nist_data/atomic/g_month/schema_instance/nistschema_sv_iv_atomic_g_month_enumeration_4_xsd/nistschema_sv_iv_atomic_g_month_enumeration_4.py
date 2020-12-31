from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xsdata.models.datatype import Period

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gMonth-enumeration-4-NS"


class NistschemaSvIvAtomicGMonthEnumeration4Type(Enum):
    VALUE_07 = Period("--07")
    VALUE_03 = Period("--03")
    VALUE_05 = Period("--05")
    VALUE_02 = Period("--02")
    VALUE_10 = Period("--10")
    VALUE_04 = Period("--04")


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
