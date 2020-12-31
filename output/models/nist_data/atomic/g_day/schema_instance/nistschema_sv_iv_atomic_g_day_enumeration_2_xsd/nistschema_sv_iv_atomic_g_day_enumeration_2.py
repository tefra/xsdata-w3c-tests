from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xsdata.models.datatype import Period

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gDay-enumeration-2-NS"


class NistschemaSvIvAtomicGDayEnumeration2Type(Enum):
    VALUE_04 = Period("---04")
    VALUE_22 = Period("---22")
    VALUE_20 = Period("---20")
    VALUE_18 = Period("---18")
    VALUE_12 = Period("---12")
    VALUE_10 = Period("---10")
    VALUE_08 = Period("---08")


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
