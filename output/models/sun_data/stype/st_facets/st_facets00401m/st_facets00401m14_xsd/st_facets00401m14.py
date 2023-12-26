from dataclasses import dataclass, field
from enum import Enum
from typing import List

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    VALUE_00 = "ງ00"
    VALUE_0 = "ງ-0"
    A0 = "ຈa0"
    VALUE_01 = "ຊ01"
    VALUE_02 = "ຍ02"
    VALUE_03 = "ດ03"
    VALUE_3 = "ຕ-3"
    A3 = "ທa3"
    VALUE_04 = "ນ04"
    VALUE_4 = "ຜ-4"
    A4 = "ຟa4"
    VALUE_05 = "ມ05"
    VALUE_5 = "ຢ-5"
    A5 = "ຣa5"
    VALUE_06 = "ລ06"
    VALUE_07 = "ວ07"
    VALUE_08 = "ສ08"
    VALUE_8 = "ສ-8"
    A8 = "ຫa8"
    VALUE_09 = "ອ09"
    VALUE_9 = "ອ-9"
    A9 = "ຮa9"


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
