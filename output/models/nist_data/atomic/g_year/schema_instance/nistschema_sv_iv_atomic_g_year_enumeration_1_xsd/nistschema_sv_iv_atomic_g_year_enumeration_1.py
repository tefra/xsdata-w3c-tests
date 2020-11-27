from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYear-enumeration-1-NS"


class NistschemaSvIvAtomicGYearEnumeration1Type(Enum):
    VALUE_2028 = "2028"
    VALUE_1999 = "1999"
    VALUE_1998 = "1998"
    VALUE_1995 = "1995"
    VALUE_2021 = "2021"
    VALUE_2006 = "2006"
    VALUE_2007 = "2007"
    VALUE_2015 = "2015"


@dataclass
class NistschemaSvIvAtomicGYearEnumeration1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYear-enumeration-1"
        namespace = "NISTSchema-SV-IV-atomic-gYear-enumeration-1-NS"

    value: Optional[NistschemaSvIvAtomicGYearEnumeration1Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
