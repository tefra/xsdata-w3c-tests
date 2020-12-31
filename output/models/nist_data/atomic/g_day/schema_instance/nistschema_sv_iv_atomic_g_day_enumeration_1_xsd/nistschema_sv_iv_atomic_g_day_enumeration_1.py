from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xsdata.models.datatype import Period

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gDay-enumeration-1-NS"


class NistschemaSvIvAtomicGDayEnumeration1Type(Enum):
    VALUE_15 = Period("---15")
    VALUE_29 = Period("---29")
    VALUE_30 = Period("---30")
    VALUE_26 = Period("---26")
    VALUE_16 = Period("---16")
    VALUE_08 = Period("---08")
    VALUE_18 = Period("---18")
    VALUE_07 = Period("---07")


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
