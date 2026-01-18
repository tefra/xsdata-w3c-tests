from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    VALUE_00 = "ະ00"
    VALUE_01 = "າ01"
    VALUE_1 = "າ-1"
    A1 = "ຳa1"
    VALUE_02 = "ຽ02"
    VALUE_03 = "ເ03"
    VALUE_3 = "ໂ-3"
    A3 = "ໄa3"
    VALUE_04 = "ཀ04"
    VALUE_4 = "གྷ-4"
    A4 = "ཇa4"
    VALUE_05 = "ཉ05"
    VALUE_5 = "ཙ-5"
    A5 = "ཀྵa5"
    VALUE_06 = "ᄀ06"
    VALUE_07 = "ᄂ07"
    VALUE_7 = "ᄂ-7"
    A7 = "ᄃa7"
    VALUE_08 = "ᄅ08"
    VALUE_8 = "ᄆ-8"
    A8 = "ᄇa8"
    VALUE_09 = "ᄉ09"


@dataclass(kw_only=True)
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
