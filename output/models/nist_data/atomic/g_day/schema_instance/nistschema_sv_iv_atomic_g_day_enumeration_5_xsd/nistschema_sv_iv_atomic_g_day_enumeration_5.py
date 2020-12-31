from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xsdata.models.datatype import Period

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gDay-enumeration-5-NS"


class NistschemaSvIvAtomicGDayEnumeration5Type(Enum):
    VALUE_21 = Period("---21")
    VALUE_23 = Period("---23")
    VALUE_13 = Period("---13")
    VALUE_26 = Period("---26")
    VALUE_24 = Period("---24")
    VALUE_18 = Period("---18")
    VALUE_30 = Period("---30")
    VALUE_14 = Period("---14")


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
