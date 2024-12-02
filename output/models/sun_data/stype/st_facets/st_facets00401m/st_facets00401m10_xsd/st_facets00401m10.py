from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    VALUE_00 = "ପ00"
    VALUE_0 = "ଭ-0"
    A0 = "ରa0"
    VALUE_01 = "ଲ01"
    VALUE_1 = "ଲ-1"
    A1 = "ଳa1"
    VALUE_02 = "ଶ02"
    VALUE_2 = "ଷ-2"
    A2 = "ହa2"
    VALUE_03 = "ଽ03"
    VALUE_04 = "ଡ଼04"
    VALUE_4 = "ଡ଼-4"
    A4 = "ଢ଼a4"
    VALUE_05 = "ୟ05"
    VALUE_5 = "ୠ-5"
    A5 = "ୡa5"
    VALUE_06 = "அ06"
    VALUE_6 = "இ-6"
    A6 = "ஊa6"
    VALUE_07 = "எ07"
    VALUE_7 = "ஏ-7"
    A7 = "ஐa7"
    VALUE_08 = "ஒ08"
    VALUE_8 = "ஓ-8"
    A8 = "கa8"
    VALUE_09 = "ங09"
    VALUE_9 = "ங-9"
    A9 = "சa9"


@dataclass
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
