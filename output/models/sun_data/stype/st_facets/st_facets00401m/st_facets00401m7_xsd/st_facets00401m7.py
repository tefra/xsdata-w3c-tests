from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    VALUE_00 = "এ00"
    VALUE_0 = "এ-0"
    A0 = "ঐa0"
    VALUE_01 = "ও01"
    VALUE_1 = "ঝ-1"
    A1 = "নa1"
    VALUE_02 = "প02"
    VALUE_2 = "ভ-2"
    A2 = "রa2"
    VALUE_03 = "ল03"
    VALUE_04 = "শ04"
    VALUE_4 = "ষ-4"
    A4 = "হa4"
    VALUE_05 = "ড়05"
    VALUE_5 = "ড়-5"
    A5 = "ঢ়a5"
    VALUE_06 = "য়06"
    VALUE_6 = "ৠ-6"
    A6 = "ৡa6"
    VALUE_07 = "ৰ07"
    VALUE_7 = "ৰ-7"
    A7 = "ৱa7"
    VALUE_08 = "ਅ08"
    VALUE_8 = "ਇ-8"
    A8 = "ਊa8"
    VALUE_09 = "ਏ09"
    VALUE_9 = "ਏ-9"
    A9 = "ਐa9"


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
