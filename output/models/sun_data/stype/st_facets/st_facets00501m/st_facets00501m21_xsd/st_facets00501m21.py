from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    A00 = "a00Ῠ"
    A0 = "a0-Ὺ"
    A0_A = "a0AῬ"
    A10 = "a10Ὸ"
    A1 = "a1-Ό"
    A1_A = "a1AΏ"
    A20 = "a20ↀ"
    A2 = "a2-ↁ"
    A2_A = "a2Aↂ"
    A30 = "a30ぁ"
    A3 = "a3-な"
    A3_A = "a3Aゔ"
    A40 = "a40ァ"
    A4 = "a4-ネ"
    A4_A = "a4Aヺ"
    A50 = "a50ㄅ"
    A5 = "a5-ㄘ"
    A5_A = "a5Aㄬ"
    A60 = "a60가"
    A6 = "a6-쇑"
    A6_A = "a6A힣"


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
