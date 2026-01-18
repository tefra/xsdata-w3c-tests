from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    VALUE_00 = "Ŋ00"
    VALUE_0 = "Ť-0"
    A0 = "ža0"
    VALUE_01 = "ƀ01"
    VALUE_1 = "Ɗ-1"
    A1 = "Ɣa1"
    VALUE_02 = "Ɩ02"
    VALUE_2 = "Ɲ-2"
    A2 = "ƥa2"
    VALUE_03 = "Ƨ03"
    VALUE_3 = "ƨ-3"
    A3 = "Ʃa3"
    VALUE_04 = "ƫ04"
    VALUE_4 = "ƴ-4"
    A4 = "ƽa4"
    VALUE_05 = "ǀ05"
    VALUE_5 = "ǁ-5"
    A5 = "ǃa5"
    VALUE_06 = "Ǎ06"
    VALUE_6 = "Ǟ-6"
    A6 = "ǯa6"
    VALUE_07 = "Ǵ07"
    VALUE_7 = "Ǵ-7"
    A7 = "ǵa7"
    VALUE_08 = "Ǻ08"
    VALUE_8 = "Ȉ-8"
    A8 = "ȗa8"
    VALUE_09 = "ɐ09"
    VALUE_9 = "ɢ-9"
    A9 = "ɴa9"


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
