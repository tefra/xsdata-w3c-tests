from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-union-short-gYear-enumeration-1-NS"


class NistschemaSvIvUnionShortGYearEnumeration1Type(Enum):
    VALUE_1990 = 1990
    VALUE_1993 = 1993
    VALUE_39 = 39
    VALUE_MINUS_962 = -962
    VALUE_384 = 384
    VALUE_1995 = 1995
    VALUE_1974 = 1974
    VALUE_2010 = 2010


@dataclass
class NistschemaSvIvUnionShortGYearEnumeration1:
    class Meta:
        name = "NISTSchema-SV-IV-union-short-gYear-enumeration-1"
        namespace = "NISTSchema-SV-IV-union-short-gYear-enumeration-1-NS"

    value: Optional[NistschemaSvIvUnionShortGYearEnumeration1Type] = field(
        default=None
    )
