from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-union-short-gYear-enumeration-4-NS"


class NistschemaSvIvUnionShortGYearEnumeration4Type(Enum):
    VALUE_MINUS_760 = -760
    VALUE_1987 = 1987
    VALUE_1974 = 1974
    VALUE_MINUS_17213 = -17213
    VALUE_MINUS_543 = -543
    VALUE_1983 = 1983
    VALUE_MINUS_2 = -2
    VALUE_442 = 442
    VALUE_MINUS_1 = -1


@dataclass(kw_only=True)
class NistschemaSvIvUnionShortGYearEnumeration4:
    class Meta:
        name = "NISTSchema-SV-IV-union-short-gYear-enumeration-4"
        namespace = "NISTSchema-SV-IV-union-short-gYear-enumeration-4-NS"

    value: NistschemaSvIvUnionShortGYearEnumeration4Type = field()
