from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-union-short-gYear-enumeration-5-NS"


class NistschemaSvIvUnionShortGYearEnumeration5Type(Enum):
    VALUE_1993 = 1993
    VALUE_1970 = 1970
    VALUE_80 = 80
    VALUE_1987 = 1987
    VALUE_2010 = 2010
    VALUE_1988 = 1988
    VALUE_1278 = 1278


@dataclass(kw_only=True)
class NistschemaSvIvUnionShortGYearEnumeration5:
    class Meta:
        name = "NISTSchema-SV-IV-union-short-gYear-enumeration-5"
        namespace = "NISTSchema-SV-IV-union-short-gYear-enumeration-5-NS"

    value: NistschemaSvIvUnionShortGYearEnumeration5Type = field()
