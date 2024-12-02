from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    VALUE_00 = "ᄋ00"
    VALUE_0 = "ᄋ-0"
    A0 = "ᄌa0"
    VALUE_01 = "ᄎ01"
    VALUE_1 = "ᄐ-1"
    A1 = "ᄒa1"
    VALUE_02 = "ᄼ02"
    VALUE_03 = "ᄾ03"
    VALUE_04 = "ᅀ04"
    VALUE_05 = "ᅌ05"
    VALUE_06 = "ᅎ06"
    VALUE_07 = "ᅐ07"
    VALUE_08 = "ᅔ08"
    VALUE_8 = "ᅔ-8"
    A8 = "ᅕa8"
    VALUE_09 = "ᅙ09"


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
