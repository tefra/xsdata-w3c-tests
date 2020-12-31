from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xsdata.models.datatype import Period

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gDay-enumeration-3-NS"


class NistschemaSvIvAtomicGDayEnumeration3Type(Enum):
    VALUE_15 = Period("---15")
    VALUE_27 = Period("---27")
    VALUE_16 = Period("---16")
    VALUE_22 = Period("---22")
    VALUE_12 = Period("---12")
    VALUE_30 = Period("---30")
    VALUE_24 = Period("---24")
    VALUE_14 = Period("---14")
    VALUE_09 = Period("---09")


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
