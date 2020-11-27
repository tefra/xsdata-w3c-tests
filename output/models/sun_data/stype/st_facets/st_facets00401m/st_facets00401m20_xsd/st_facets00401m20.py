from dataclasses import dataclass, field
from enum import Enum
from typing import List

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    VALUE_00 = "Ὓ00"
    VALUE_01 = "Ὕ01"
    VALUE_02 = "Ὗ02"
    VALUE_2 = "Ὦ-2"
    A2 = "ώa2"
    VALUE_03 = "ᾰ03"
    VALUE_3 = "ᾰ-3"
    A3 = "ᾱa3"
    VALUE_04 = "Ᾰ04"
    VALUE_4 = "Ᾱ-4"
    A4 = "Άa4"
    VALUE_05 = "Ὲ05"
    VALUE_5 = "Έ-5"
    A5 = "Ήa5"
    VALUE_06 = "ῐ06"
    VALUE_6 = "ῐ-6"
    A6 = "ῑa6"
    VALUE_07 = "Ῐ07"
    VALUE_7 = "Ῑ-7"
    A7 = "Ίa7"
    VALUE_08 = "ῠ08"
    VALUE_8 = "ῠ-8"
    A8 = "ῡa8"
    VALUE_09 = "ῥ09"


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
