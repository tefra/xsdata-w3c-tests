from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xsdata.models.datatype import Period

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gMonth-enumeration-5-NS"


class NistschemaSvIvAtomicGMonthEnumeration5Type(Enum):
    VALUE_06 = Period("--06")
    VALUE_05 = Period("--05")
    VALUE_02 = Period("--02")
    VALUE_01 = Period("--01")


@dataclass
class NistschemaSvIvAtomicGMonthEnumeration5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gMonth-enumeration-5"
        namespace = "NISTSchema-SV-IV-atomic-gMonth-enumeration-5-NS"

    value: Optional[NistschemaSvIvAtomicGMonthEnumeration5Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
