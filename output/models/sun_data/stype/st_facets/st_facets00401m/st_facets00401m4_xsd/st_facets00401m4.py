from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    VALUE_00 = "ϐ00"
    VALUE_0 = "ϓ-0"
    A0 = "ϖa0"
    VALUE_01 = "Ϣ01"
    VALUE_1 = "ϩ-1"
    A1 = "ϱa1"
    VALUE_02 = "Ё02"
    VALUE_2 = "І-2"
    A2 = "Ќa2"
    VALUE_03 = "Ў03"
    VALUE_3 = "Ю-3"
    A3 = "яa3"
    VALUE_04 = "ё04"
    VALUE_4 = "і-4"
    A4 = "ќa4"
    VALUE_05 = "ў05"
    VALUE_5 = "ѯ-5"
    A5 = "ҁa5"
    VALUE_06 = "Ґ06"
    VALUE_6 = "ҧ-6"
    A6 = "ҿa6"
    VALUE_07 = "Ӂ07"
    VALUE_7 = "ӂ-7"
    A7 = "ӄa7"
    VALUE_08 = "Ӈ08"
    VALUE_8 = "Ӈ-8"
    A8 = "ӈa8"
    VALUE_09 = "Ӌ09"
    VALUE_9 = "Ӌ-9"
    A9 = "ӌa9"


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
