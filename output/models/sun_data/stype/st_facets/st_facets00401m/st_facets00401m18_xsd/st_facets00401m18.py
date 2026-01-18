from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    VALUE_00 = "ᆫ00"
    VALUE_01 = "ᆮ01"
    VALUE_1 = "ᆮ-1"
    A1 = "ᆯa1"
    VALUE_02 = "ᆷ02"
    VALUE_2 = "ᆷ-2"
    A2 = "ᆸa2"
    VALUE_03 = "ᆺ03"
    VALUE_04 = "ᆼ04"
    VALUE_4 = "ᆿ-4"
    A4 = "ᇂa4"
    VALUE_05 = "ᇫ05"
    VALUE_06 = "ᇰ06"
    VALUE_07 = "ᇹ07"
    VALUE_08 = "Ḁ08"
    VALUE_8 = "Ṋ-8"
    A8 = "ẕa8"
    VALUE_09 = "ẛ09"


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
