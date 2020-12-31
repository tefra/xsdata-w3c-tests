from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xsdata.models.datatype import Period

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYear-enumeration-2-NS"


class NistschemaSvIvAtomicGYearEnumeration2Type(Enum):
    VALUE_2007 = Period("2007")
    VALUE_2020 = Period("2020")
    VALUE_1999 = Period("1999")
    VALUE_2011 = Period("2011")
    VALUE_1976 = Period("1976")
    VALUE_1984 = Period("1984")
    VALUE_1972 = Period("1972")
    VALUE_1992 = Period("1992")
    VALUE_2018 = Period("2018")


@dataclass
class NistschemaSvIvAtomicGYearEnumeration2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYear-enumeration-2"
        namespace = "NISTSchema-SV-IV-atomic-gYear-enumeration-2-NS"

    value: Optional[NistschemaSvIvAtomicGYearEnumeration2Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
