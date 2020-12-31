from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xsdata.models.datatype import Period

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gMonth-enumeration-1-NS"


class NistschemaSvIvAtomicGMonthEnumeration1Type(Enum):
    VALUE_01 = Period("--01")
    VALUE_08 = Period("--08")
    VALUE_02 = Period("--02")
    VALUE_05 = Period("--05")
    VALUE_04 = Period("--04")


@dataclass
class NistschemaSvIvAtomicGMonthEnumeration1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gMonth-enumeration-1"
        namespace = "NISTSchema-SV-IV-atomic-gMonth-enumeration-1-NS"

    value: Optional[NistschemaSvIvAtomicGMonthEnumeration1Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
