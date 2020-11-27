from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-union-short-gYear-enumeration-3-NS"


class NistschemaSvIvUnionShortGYearEnumeration3Type(Enum):
    VALUE_1978 = "1978"
    VALUE_1988 = "1988"
    VALUE_MINUS_13234 = "-13234"
    VALUE_MINUS_1 = "-1"
    VALUE_509 = "509"
    VALUE_36 = "36"
    VALUE_MINUS_167 = "-167"
    VALUE_1974 = "1974"
    VALUE_MINUS_17213 = "-17213"


@dataclass
class NistschemaSvIvUnionShortGYearEnumeration3:
    class Meta:
        name = "NISTSchema-SV-IV-union-short-gYear-enumeration-3"
        namespace = "NISTSchema-SV-IV-union-short-gYear-enumeration-3-NS"

    value: Optional[NistschemaSvIvUnionShortGYearEnumeration3Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
