from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xsdata.models.datatype import Period

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYear-enumeration-4-NS"


class NistschemaSvIvAtomicGYearEnumeration4Type(Enum):
    VALUE_1978 = Period("1978")
    VALUE_2027 = Period("2027")
    VALUE_2007 = Period("2007")
    VALUE_1970 = Period("1970")
    VALUE_2021 = Period("2021")
    VALUE_2016 = Period("2016")
    VALUE_2014 = Period("2014")
    VALUE_2015 = Period("2015")
    VALUE_2023 = Period("2023")
    VALUE_2002 = Period("2002")


@dataclass
class NistschemaSvIvAtomicGYearEnumeration4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYear-enumeration-4"
        namespace = "NISTSchema-SV-IV-atomic-gYear-enumeration-4-NS"

    value: Optional[NistschemaSvIvAtomicGYearEnumeration4Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
