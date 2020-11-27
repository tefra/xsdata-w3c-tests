from dataclasses import dataclass, field
from enum import Enum
from typing import List

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    VALUE_00 = "എ00"
    VALUE_0 = "ഏ-0"
    A0 = "ഐa0"
    VALUE_01 = "ഒ01"
    VALUE_1 = "ഝ-1"
    A1 = "നa1"
    VALUE_02 = "പ02"
    VALUE_2 = "റ-2"
    A2 = "ഹa2"
    VALUE_03 = "ൠ03"
    VALUE_3 = "ൠ-3"
    A3 = "ൡa3"
    VALUE_04 = "ก04"
    VALUE_4 = "ท-4"
    A4 = "ฮa4"
    VALUE_05 = "ะ05"
    VALUE_06 = "า06"
    VALUE_6 = "า-6"
    A6 = "ำa6"
    VALUE_07 = "เ07"
    VALUE_7 = "โ-7"
    A7 = "ๅa7"
    VALUE_08 = "ກ08"
    VALUE_8 = "ກ-8"
    A8 = "ຂa8"
    VALUE_09 = "ຄ09"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "SType/ST_facets"

    value: List[S] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )
