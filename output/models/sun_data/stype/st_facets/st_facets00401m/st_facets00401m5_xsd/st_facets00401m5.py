from dataclasses import dataclass, field
from enum import Enum
from typing import List

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    VALUE_00 = "Ӑ00"
    VALUE_0 = "ӝ-0"
    A0 = "ӫa0"
    VALUE_01 = "Ӯ01"
    VALUE_1 = "ӱ-1"
    A1 = "ӵa1"
    VALUE_02 = "Ӹ02"
    VALUE_2 = "Ӹ-2"
    A2 = "ӹa2"
    VALUE_03 = "Ա03"
    VALUE_3 = "Ճ-3"
    A3 = "Ֆa3"
    VALUE_04 = "ՙ04"
    VALUE_05 = "ա05"
    VALUE_5 = "ճ-5"
    A5 = "ֆa5"
    VALUE_06 = "א06"
    VALUE_6 = "ם-6"
    A6 = "תa6"
    VALUE_07 = "װ07"
    VALUE_7 = "ױ-7"
    A7 = "ײa7"
    VALUE_08 = "ء08"
    VALUE_8 = "ح-8"
    A8 = "غa8"
    VALUE_09 = "ف09"
    VALUE_9 = "م-9"
    A9 = "يa9"


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
