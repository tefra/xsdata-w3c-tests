from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    VALUE_00 = "એ00"
    VALUE_0 = "ઐ-0"
    A0 = "ઑa0"
    VALUE_01 = "ઓ01"
    VALUE_1 = "ઝ-1"
    A1 = "નa1"
    VALUE_02 = "પ02"
    VALUE_2 = "ભ-2"
    A2 = "રa2"
    VALUE_03 = "લ03"
    VALUE_3 = "લ-3"
    A3 = "ળa3"
    VALUE_04 = "વ04"
    VALUE_4 = "ષ-4"
    A4 = "હa4"
    VALUE_05 = "ઽ05"
    VALUE_06 = "ૠ06"
    VALUE_07 = "ଅ07"
    VALUE_7 = "ଈ-7"
    A7 = "ଌa7"
    VALUE_08 = "ଏ08"
    VALUE_8 = "ଏ-8"
    A8 = "ଐa8"
    VALUE_09 = "ଓ09"
    VALUE_9 = "ଝ-9"
    A9 = "ନa9"


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
