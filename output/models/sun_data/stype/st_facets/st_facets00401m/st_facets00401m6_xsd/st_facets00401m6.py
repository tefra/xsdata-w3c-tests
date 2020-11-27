from dataclasses import dataclass, field
from enum import Enum
from typing import List

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    VALUE_00 = "ٱ00"
    VALUE_0 = "ڔ-0"
    A0 = "ڷa0"
    VALUE_01 = "ں01"
    VALUE_1 = "ڼ-1"
    A1 = "ھa1"
    VALUE_02 = "ۀ02"
    VALUE_2 = "ۇ-2"
    A2 = "ێa2"
    VALUE_03 = "ې03"
    VALUE_3 = "ۑ-3"
    A3 = "ۓa3"
    VALUE_04 = "ە04"
    VALUE_05 = "ۥ05"
    VALUE_5 = "ۥ-5"
    A5 = "ۦa5"
    VALUE_06 = "अ06"
    VALUE_6 = "ट-6"
    A6 = "हa6"
    VALUE_07 = "ऽ07"
    VALUE_08 = "क़08"
    VALUE_8 = "ड़-8"
    A8 = "ॡa8"
    VALUE_09 = "অ09"
    VALUE_9 = "ঈ-9"
    A9 = "ঌa9"


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
