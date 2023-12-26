from dataclasses import dataclass, field
from enum import Enum
from typing import List

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    VALUE_00 = "ɶ00"
    VALUE_0 = "ɺ-0"
    A0 = "ɿa0"
    VALUE_01 = "ʁ01"
    VALUE_1 = "ʔ-1"
    A1 = "ʨa1"
    VALUE_02 = "ʻ02"
    VALUE_2 = "ʾ-2"
    A2 = "ˁa2"
    VALUE_03 = "Ά03"
    VALUE_04 = "Έ04"
    VALUE_4 = "Ή-4"
    A4 = "Ίa4"
    VALUE_05 = "Ό05"
    VALUE_06 = "Ύ06"
    VALUE_6 = "Ύ-6"
    A6 = "Ώa6"
    VALUE_07 = "Α07"
    VALUE_7 = "Ι-7"
    A7 = "Ρa7"
    VALUE_08 = "Σ08"
    VALUE_8 = "Ω-8"
    A8 = "ίa8"
    VALUE_09 = "α09"
    VALUE_9 = "ο-9"
    A9 = "ώa9"


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
