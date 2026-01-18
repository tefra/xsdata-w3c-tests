from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    A000 = "a000"
    A0_4 = "a0-4"
    A0_A9 = "a0A9"
    A10 = "a10٠"
    A1 = "a1-٤"
    A1_A = "a1A٩"
    A20 = "a20۰"
    A2 = "a2-۴"
    A2_A = "a2A۹"
    A30 = "a30०"
    A3 = "a3-४"
    A3_A = "a3A९"
    A40 = "a40০"
    A4 = "a4-৪"
    A4_A = "a4A৯"
    A50 = "a50੦"
    A5 = "a5-੪"
    A5_A = "a5A੯"
    A60 = "a60૦"
    A6 = "a6-૪"
    A6_A = "a6A૯"
    A70 = "a70୦"
    A7 = "a7-୪"
    A7_A = "a7A୯"
    A80 = "a80௧"
    A8 = "a8-௫"
    A8_A = "a8A௯"
    A90 = "a90౦"
    A9 = "a9-౪"
    A9_A = "a9A౯"


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
