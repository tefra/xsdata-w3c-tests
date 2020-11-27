from dataclasses import dataclass, field
from enum import Enum
from typing import List

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    VALUE_00 = "ᅟ00"
    VALUE_0 = "ᅠ-0"
    A0 = "ᅡa0"
    VALUE_01 = "ᅣ01"
    VALUE_02 = "ᅥ02"
    VALUE_03 = "ᅧ03"
    VALUE_04 = "ᅩ04"
    VALUE_05 = "ᅭ05"
    VALUE_5 = "ᅭ-5"
    A5 = "ᅮa5"
    VALUE_06 = "ᅲ06"
    VALUE_6 = "ᅲ-6"
    A6 = "ᅳa6"
    VALUE_07 = "ᅵ07"
    VALUE_08 = "ᆞ08"
    VALUE_09 = "ᆨ09"


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
