from dataclasses import dataclass, field
from enum import Enum
from typing import List

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    VALUE_00 = "Ῠ00"
    VALUE_0 = "Ὺ-0"
    A0 = "Ῥa0"
    VALUE_01 = "Ὸ01"
    VALUE_1 = "Ό-1"
    A1 = "Ώa1"
    VALUE_02 = "ↀ02"
    VALUE_2 = "ↁ-2"
    A2 = "ↂa2"
    VALUE_03 = "ぁ03"
    VALUE_3 = "な-3"
    A3 = "ゔa3"
    VALUE_04 = "ァ04"
    VALUE_4 = "ネ-4"
    A4 = "ヺa4"
    VALUE_05 = "ㄅ05"
    VALUE_5 = "ㄘ-5"
    A5 = "ㄬa5"
    VALUE_06 = "가06"
    VALUE_6 = "쇑-6"
    A6 = "힣a6"


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
