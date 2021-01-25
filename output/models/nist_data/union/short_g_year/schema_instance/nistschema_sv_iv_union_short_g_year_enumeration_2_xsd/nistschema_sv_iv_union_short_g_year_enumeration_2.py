from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-union-short-gYear-enumeration-2-NS"


class NistschemaSvIvUnionShortGYearEnumeration2Type(Enum):
    VALUE_MINUS_3830 = -3830
    VALUE_1970 = 1970
    VALUE_MINUS_37 = -37
    VALUE_MINUS_205 = -205
    VALUE_MINUS_8 = -8
    VALUE_MINUS_4097 = -4097


@dataclass
class NistschemaSvIvUnionShortGYearEnumeration2:
    class Meta:
        name = "NISTSchema-SV-IV-union-short-gYear-enumeration-2"
        namespace = "NISTSchema-SV-IV-union-short-gYear-enumeration-2-NS"

    value: Optional[NistschemaSvIvUnionShortGYearEnumeration2Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
