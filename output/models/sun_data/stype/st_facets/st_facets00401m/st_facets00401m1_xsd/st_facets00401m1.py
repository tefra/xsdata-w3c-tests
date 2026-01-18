from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    A00 = "A00"
    M_0 = "M-0"
    ZA0 = "Za0"
    A01 = "a01"
    D_1 = "d-1"
    HA1 = "ha1"
    J02 = "j02"
    R_2 = "r-2"
    ZA2 = "za2"
    VALUE_03 = "À03"
    VALUE_3 = "Ë-3"
    A3 = "Öa3"
    VALUE_04 = "Ø04"
    VALUE_4 = "Û-4"
    A4 = "Þa4"
    VALUE_05 = "à05"
    VALUE_5 = "ë-5"
    A5 = "öa5"
    VALUE_06 = "ø06"
    VALUE_6 = "û-6"
    A6 = "ÿa6"
    VALUE_07 = "Ā07"
    VALUE_7 = "Ę-7"
    A7 = "ıa7"
    VALUE_08 = "Ĵ08"
    VALUE_8 = "Ĺ-8"
    A8 = "ľa8"
    VALUE_09 = "Ł09"
    VALUE_9 = "ń-9"
    A9 = "ňa9"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "SType/ST_facets"

    value: list[S] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
