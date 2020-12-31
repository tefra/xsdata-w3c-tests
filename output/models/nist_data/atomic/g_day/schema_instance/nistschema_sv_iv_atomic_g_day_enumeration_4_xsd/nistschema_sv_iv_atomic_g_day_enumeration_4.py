from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xsdata.models.datatype import Period

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gDay-enumeration-4-NS"


class NistschemaSvIvAtomicGDayEnumeration4Type(Enum):
    VALUE_15 = Period("---15")
    VALUE_05 = Period("---05")
    VALUE_17 = Period("---17")
    VALUE_12 = Period("---12")
    VALUE_21 = Period("---21")
    VALUE_18 = Period("---18")


@dataclass
class NistschemaSvIvAtomicGDayEnumeration4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gDay-enumeration-4"
        namespace = "NISTSchema-SV-IV-atomic-gDay-enumeration-4-NS"

    value: Optional[NistschemaSvIvAtomicGDayEnumeration4Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
