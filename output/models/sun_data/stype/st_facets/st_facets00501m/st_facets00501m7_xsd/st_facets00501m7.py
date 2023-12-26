from dataclasses import dataclass, field
from enum import Enum
from typing import List

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    A00 = "a00এ"
    A0 = "a0-এ"
    A0_A = "a0Aঐ"
    A10 = "a10ও"
    A1 = "a1-ঝ"
    A1_A = "a1Aন"
    A20 = "a20প"
    A2 = "a2-ভ"
    A2_A = "a2Aর"
    A30 = "a30ল"
    A40 = "a40শ"
    A4 = "a4-ষ"
    A4_A = "a4Aহ"
    A50 = "a50ড়"
    A5 = "a5-ড়"
    A5_A = "a5Aঢ়"
    A60 = "a60য়"
    A6 = "a6-ৠ"
    A6_A = "a6Aৡ"
    A70 = "a70ৰ"
    A7 = "a7-ৰ"
    A7_A = "a7Aৱ"
    A80 = "a80ਅ"
    A8 = "a8-ਇ"
    A8_A = "a8Aਊ"
    A90 = "a90ਏ"
    A9 = "a9-ਏ"
    A9_A = "a9Aਐ"


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
        },
    )
