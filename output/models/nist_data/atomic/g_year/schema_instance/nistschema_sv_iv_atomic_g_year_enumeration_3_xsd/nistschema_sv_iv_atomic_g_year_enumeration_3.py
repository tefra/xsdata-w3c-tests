from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xsdata.models.datatype import Period

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYear-enumeration-3-NS"


class NistschemaSvIvAtomicGYearEnumeration3Type(Enum):
    VALUE_2004 = Period("2004")
    VALUE_2014 = Period("2014")
    VALUE_1991 = Period("1991")
    VALUE_2001 = Period("2001")
    VALUE_2021 = Period("2021")


@dataclass
class NistschemaSvIvAtomicGYearEnumeration3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYear-enumeration-3"
        namespace = "NISTSchema-SV-IV-atomic-gYear-enumeration-3-NS"

    value: Optional[NistschemaSvIvAtomicGYearEnumeration3Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
