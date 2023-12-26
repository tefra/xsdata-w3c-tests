from dataclasses import dataclass, field
from enum import Enum
from typing import List

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    VALUE_00 = "Ạ00"
    VALUE_0 = "Ọ-0"
    A0 = "ỹa0"
    VALUE_01 = "ἀ01"
    VALUE_1 = "Ἂ-1"
    A1 = "ἕa1"
    VALUE_02 = "Ἐ02"
    VALUE_2 = "Ἒ-2"
    A2 = "Ἕa2"
    VALUE_03 = "ἠ03"
    VALUE_3 = "ἲ-3"
    A3 = "ὅa3"
    VALUE_04 = "Ὀ04"
    VALUE_4 = "Ὂ-4"
    A4 = "Ὅa4"
    VALUE_05 = "ὑ05"
    VALUE_06 = "ὓ06"
    VALUE_07 = "ὕ07"
    VALUE_08 = "ὗ08"
    VALUE_09 = "Ὑ09"


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
        },
    )
